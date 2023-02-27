import random
import itertools


class Field:
    def __init__(self, width: int, height: int):
        self._width: int = width
        self._height: int = height
        self._field: list[list[bool]] = [[False] * width for _ in range(height)]

        self._previous_states = set()
        self._repeats = False

    @classmethod
    def from_random(cls, width: int, height: int, fill: float = 0.5):
        filled_per_row = int(fill * width)
        row_values = [True] * filled_per_row + [False] * (width - filled_per_row)

        obj = cls(width, height)
        obj._field = [random.sample(row_values, width) for _ in range(height)]

        return obj

    def step(self):
        new_field = [[False] * self._width for _ in range(self._height)]

        for y, row in enumerate(self._field):
            for x, e in enumerate(row):
                neighbours_count = self.count_neighbours(x, y)
                if not e and neighbours_count == 3:
                    new_field[y][x] = True
                elif e and neighbours_count in (2, 3):
                    new_field[y][x] = True

        field_hash = self.get_field_hash(new_field)
        if field_hash in self._previous_states:
            self._repeats = True
        self._previous_states.add(field_hash)

        self._field = new_field

    def count_neighbours(self, x: int, y: int):
        return sum(self._field[(y + dy) % self._height][(x + dx) % self.width]
                   for dx, dy in itertools.product((-1, 0, 1), repeat=2) if dx or dy)

    @staticmethod
    def get_field_hash(field: list[list[int]]):
        return hash(tuple(e for row in field for e in row))

    @property
    def repeats(self):
        return self._repeats

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def field(self):
        return self._field.copy()
