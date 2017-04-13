import numpy as np

from itertools import count

from ..library.number_theory.pythagorean_triples import \
    primitive_pythagorean_triples, PythagoreanTriplet


def solve(bound: int=1_500_000, multiplicity: int=1) -> int:
    def valid(triplet: PythagoreanTriplet) -> bool:
        return sum(triplet) <= bound

    multiplicities = np.zeros(bound + 1, np.int64)

    generator = primitive_pythagorean_triples(valid)

    for triplet in generator:
        perimeter = sum(triplet)

        multiplicities[perimeter::perimeter] += 1

    return sum(multiplicities == multiplicity)
