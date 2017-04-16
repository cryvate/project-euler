from fractions import Fraction
from itertools import chain, cycle

from typing import Generator, Iterable, List, Tuple

from ..sqrt import sqrt


def convergent_sequence(generator: Iterable[int]) -> \
        Generator[Fraction, None, None]:
    h = (0, 1)
    k = (1, 0)

    for a in generator:
        h = h[1], a * h[1] + h[0]
        k = k[1], a * k[1] + k[0]

        yield Fraction(h[-1], k[-1])


def continued_fraction_sqrt(n: int) -> Tuple[List[int], List[int]]:
    sqrt_n = sqrt(n)
    remainders = []
    remainder = (0, 1)
    # remainder is an + (sqrt(n) - p) / q and these are initial.
    continued_fraction = []

    while remainder not in remainders:
        remainders.append(remainder)
        p, q = remainder

        q = (n - (p * p)) // q
        a = int((sqrt_n + p) / q)
        p = a * q - p

        continued_fraction.append(a)

        remainder = (p, q)

    index = remainders.index(remainder)

    return continued_fraction[1:index], continued_fraction[index:]


def convergents_sqrt(n: int) -> Generator[Fraction, None, None]:
    initial, repeat = continued_fraction_sqrt(n)
    convergents = convergent_sequence(chain(initial, cycle(repeat)))

    yield from convergents
