from fractions import Fraction

from typing import Generator


def convergent_sequence(a_0: int) -> Generator[Fraction, int, None]:
    a = a_0

    h = (0, 1)
    k = (1, 0)

    while True:
        h = h[1], a * h[1] + h[0]
        k = k[1], a * k[1] + k[0]

        a = yield Fraction(h[-1], k[-1])
