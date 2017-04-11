from math import floor, sqrt
from fractions import Fraction

from typing import Generator, Iterable, List, Tuple


def convergent_sequence(generator: Iterable[int]) -> \
        Generator[Fraction, int, None]:
    h = (0, 1)
    k = (1, 0)

    for a in generator:
        h = h[1], a * h[1] + h[0]
        k = k[1], a * k[1] + k[0]

        yield Fraction(h[-1], k[-1])


def continued_fraction_sqrt(n: int) -> Tuple[List[int], List[int]]:
    remainders = []
    continued_fraction = []
    remainder = (Fraction(1), Fraction(0))  # remainder is sqrt(n) + 0.

    while remainder not in remainders:
        remainders.append(remainder)

        a = int(floor(remainder[0] * sqrt(n) + remainder[1]))
        continued_fraction.append(a)

        norm = (remainder[1] - a) ** 2 - remainder[0] ** 2 * n
        remainder = (-remainder[0] / norm, (remainder[1] - a) / norm)

    index = remainders.index(remainder)

    return continued_fraction[:index], continued_fraction[index:]
