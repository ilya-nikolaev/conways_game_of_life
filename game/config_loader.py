import json
from dataclasses import dataclass


@dataclass
class GameConfig:
    cell_width: int
    cell_height: int

    cell_side: int

    auto_restart: bool
    fullscreen: bool
    max_game_speed: int

    random_fill_part: float

    @property
    def window_size(self):
        return self.cell_width * self.cell_side, self.cell_height * self.cell_side


def load_config() -> GameConfig:
    with open("config.json", "r", encoding="UTF-8") as file:
        config_data = json.load(file)

    return GameConfig(**config_data)
