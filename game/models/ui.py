import pygame

from game.config_loader import load_config
from game.models.field import Field

PALETTE = ((0, 0, 0), (0, 255, 0))


class UI:
    def __init__(self):
        pygame.init()

        self.config = load_config()

        self.screen = pygame.display.set_mode(self.config.window_size)
        self.clock = pygame.time.Clock()

        self._field = Field.from_random(self.config.cell_width, self.config.cell_height, self.config.random_fill_part)
        self.running = True
        self.pause = False

    def run(self):
        while self.running:
            self.handle_events()

            if not self.pause:
                self.draw()
                self._field.step()

            if self._field.repeats and self.config.auto_restart:
                self._field = Field.from_random(self.config.cell_width, self.config.cell_height)

            self.clock.tick(self.config.max_game_speed)

    def draw(self):
        for y, row in enumerate(self._field.field):
            for x, e in enumerate(row):
                pygame.draw.rect(self.screen, PALETTE[e], self.get_cell_rect(x, y))

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.pause = not self.pause
                if event.button == 3:
                    self.restart()

    def get_cell_rect(self, x: int, y: int) -> pygame.rect.Rect:
        return pygame.rect.Rect(
            x * self.config.cell_side,
            y * self.config.cell_side,
            self.config.cell_side,
            self.config.cell_side)

    def restart(self):
        self._field = Field.from_random(self.config.cell_width, self.config.cell_height, 0.5)
