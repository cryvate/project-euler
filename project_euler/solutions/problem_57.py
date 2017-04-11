from itertools import chain, cycle

from ..library.number_theory.continued_fractions import convergent_sequence
from ..library.base import number_to_list


def solve(bound: int=1000) -> int:
    generator = convergent_sequence(chain([1], cycle([2])))

    count = 0

    for i, convergent in enumerate(generator):
        if i >= bound:
            return count

        numerator, denominator = convergent.numerator, convergent.denominator

        if len(number_to_list(numerator)) > len(number_to_list(denominator)):
            count += 1
