import itertools

import numpy as np


class Field:
    def __init__(self, width: int, height: int):
        self._width: int = width
        self._height: int = height
        self._field = np.zeros(self.size, dtype=int)

        self._previous_states = set()
        self._repeats = False

    @classmethod
    def from_random(cls, width: int, height: int, fill: float = 0.5):
        filled_per_row = int(fill * width)
        row_values = np.zeros(width, dtype=int)
        row_values[:filled_per_row] = np.ones(filled_per_row, dtype=int)

        obj = cls(width, height)
        for i in range(height):
            obj._field[i] = np.random.choice(row_values, width)

        return obj

    def step(self):
        new_field = np.zeros(self.size, dtype=int)
        neighbours_count = self.count_neighbours()

        mask = np.logical_and(self._field == 1, np.logical_or(neighbours_count == 2, neighbours_count == 3))
        new_field[mask] = True
        mask = np.logical_and(self._field == 0, neighbours_count == 3)
        new_field[mask] = True

        field_hash = self.get_field_hash(new_field)
        if field_hash in self._previous_states:
            self._repeats = True
        self._previous_states.add(field_hash)

        self._field = new_field

    def count_neighbours(self) -> np.ndarray:
        return sum(np.roll(self._field, shift, axis=(0, 1))
                   for shift in itertools.product((-1, 0, 1), repeat=2) if any(shift))

    @staticmethod
    def get_field_hash(field: np.ndarray) -> int:
        # noinspection PyTypeChecker
        list_field: list[list[int]] = field.tolist()
        return hash(tuple(e for row in list_field for e in row))

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
    def size(self):
        return self._height, self._width

    @property
    def field(self):
        return self._field.copy()
