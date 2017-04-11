from fractions import Fraction
import pytest

from typing import List, Tuple

from .continued_fractions import convergent_sequence, \
                                 continued_fraction_sqrt


CONVERGENTS = [
    (
        [0, 1, 5, 2, 2],
        [Fraction(0, 1),
         Fraction(1, 1),
         Fraction(5, 6),
         Fraction(11, 13),
         Fraction(27, 32)]
    )
]


CONTINUED_FRACTIONS_ROOTS = [
    (
        2,
        (
            [1],
            [2]
        )
    ),
    (
        3,
        (
            [1],
            [1, 2],
        )
    ),
    (
        5,
        (
            [2],
            [4],
        )
    ),
    (
        6,
        (
            [2],
            [2, 4],
        )
    ),
    (
        7,
        (
            [2],
            [1, 1, 1, 4],
        )
    ),
    (
        8,
        (
            [2],
            [1, 4],
        )
    ),
    (
        10,
        (
            [3],
            [6],
        )
    ),
    (
        11,
        (
            [3],
            [3, 6],
        )
    ),
    (
        12,
        (
            [3],
            [2, 6],
        )
    ),
    (
        13,
        (
            [3],
            [1, 1, 1, 1, 6],
        )
    ),
]


@pytest.mark.parametrize('a,convergent', CONVERGENTS)
def test_convergents(a: List[int], convergent: List[Fraction]) -> None:
    generator = convergent_sequence(a[0])

    assert next(generator) == convergent[0]

    for i in range(1, len(convergent)):
        assert generator.send(a[i]) == convergent[i]


@pytest.mark.parametrize('n,expected_output', CONTINUED_FRACTIONS_ROOTS)
def test_continued_fraction_sqrt(n: int,
                                 expected_output: Tuple[List[int], List[int]])\
        -> None:
    assert continued_fraction_sqrt(n) == expected_output
