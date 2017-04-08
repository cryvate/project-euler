from itertools import product
import pytest

from fractions import Fraction


from .fraction_representation import Representation, \
                                     unit_fraction_to_representation, \
                                     fraction_to_representation, \
                                     representation_to_fraction


NUMERATORS_DENOMINATORS = [(x, y) for x, y in
                           product(range(15), range(1, 15)) if x < y]


def representation_to_decimal(representation: Representation,
                              base: int=10) -> float:
    if representation[1][1] == 0:
        return representation[0][0] * base ** -representation[0][1]

    return representation[0][0] * base ** -representation[0][1] + \
        representation[1][0] * base ** -representation[0][1] * \
        base ** -representation[1][1] / \
        (1 - base ** -representation[1][1])


@pytest.mark.parametrize('denominator',
                         range(2, 100))
def test_unit_fraction_to_representation(denominator: int) -> None:
    representation = unit_fraction_to_representation(denominator)
    decimal = representation_to_decimal(representation)

    assert decimal == pytest.approx(1 / denominator)


@pytest.mark.parametrize('numerator,denominator', NUMERATORS_DENOMINATORS)
def test_fraction_to_representation(numerator: int, denominator: int) -> None:
    fraction = Fraction(numerator, denominator)
    representation = fraction_to_representation(fraction)
    decimal = representation_to_decimal(representation)

    assert decimal == pytest.approx(numerator / denominator)


@pytest.mark.parametrize('numerator,denominator', NUMERATORS_DENOMINATORS)
def test_representation_to_fraction(numerator: int, denominator: int) -> None:
    fraction = Fraction(numerator, denominator)
    representation = fraction_to_representation(fraction)
    fraction_back = representation_to_fraction(representation)
    decimal = representation_to_decimal(representation)

    assert float(fraction_back) == pytest.approx(decimal)
