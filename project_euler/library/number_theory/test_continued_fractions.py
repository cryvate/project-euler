from fractions import Fraction
import pytest

from typing import List

from .continued_fractions import convergent_sequence


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


@pytest.mark.parametrize('a,convergent', CONVERGENTS)
def test_convergents(a: List[int], convergent: List[Fraction]):
    generator = convergent_sequence(a[0])

    assert next(generator) == convergent[0]

    for i in range(1, len(convergent)):
        assert generator.send(a[i]) == convergent[i]
