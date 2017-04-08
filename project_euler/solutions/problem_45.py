from typing import List

from ..library.sequences import triangle_sequence, \
                                pentagonal_sequence, \
                                hexagonal_sequence


def solve(ignore: List[int]=[0, 1, 40755]) -> int:
    pentagonal_generator = pentagonal_sequence()
    hexagonal_generator = hexagonal_sequence()

    pentagonal_number = next(pentagonal_generator)
    hexagonal_number = next(hexagonal_generator)

    for triangle_number in triangle_sequence():
        while pentagonal_number < triangle_number:
            pentagonal_number = next(pentagonal_generator)

        while hexagonal_number < triangle_number:
            hexagonal_number = next(hexagonal_generator)

        if triangle_number == pentagonal_number and \
                pentagonal_number == hexagonal_number and \
                triangle_number not in ignore:
            return triangle_number
