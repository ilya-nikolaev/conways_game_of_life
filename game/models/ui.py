import pygame

from game.models.field import Field

CELL_WIDTH = 128
CELL_HEIGHT = 128

CELL_SIDE = 4

SIZE = WIDTH, HEIGHT = CELL_WIDTH * CELL_SIDE, CELL_HEIGHT * CELL_SIDE
FPS = 60

PALETTE = ((0, 0, 0), (0, 255, 0))


class UI:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()

        self._field = Field.from_random(CELL_WIDTH, CELL_HEIGHT, 0.2)
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()

            self.draw()
            self._field.step()

            if self._field.repeats:
                self._field = Field.from_random(CELL_WIDTH, CELL_HEIGHT)

            self.clock.tick(FPS)

    def draw(self):
        for y, row in enumerate(self._field.field):
            for x, e in enumerate(row):
                pygame.draw.rect(self.screen, PALETTE[e], self.get_cell_rect(x, y))

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    @staticmethod
    def get_cell_rect(x: int, y: int) -> pygame.rect.Rect:
        return pygame.rect.Rect(x * CELL_SIDE, y * CELL_SIDE, CELL_SIDE, CELL_SIDE)
