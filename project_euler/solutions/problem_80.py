from fractions import Fraction

from ..library.base import number_to_list
from ..library.sqrt import is_square
from ..library.number_theory.continued_fractions import convergents_sqrt


def solve(bound: int=100, digits: int=100, base: int=10):
    sufficient = base ** digits

    accumulate = 0

    for n in range(bound + 1):
        if is_square(n):
            continue

        for convergent in convergents_sqrt(n):
            if convergent.denominator > sufficient:
                break

        while convergent > 1:
            convergent *= Fraction(1, base)

        remainder = Fraction(0, 1)
        power = Fraction(1, 1)

        for digit in range(1, digits + 1):
            power *= Fraction(1, base)

            while convergent - power >= 0:
                remainder += power
                convergent -= power

        accumulate += sum(number_to_list(remainder.numerator *
                                         (sufficient // remainder.denominator),
                                         base))

    return accumulate
