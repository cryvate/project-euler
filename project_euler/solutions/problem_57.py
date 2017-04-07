from ..library.number_theory.continued_fractions import convergent_sequence
from ..library.base import number_to_list


def solve(bound: int=1000) -> int:
    generator = convergent_sequence(1)

    count = 0

    next(generator)

    for i in range(bound):
        convergent = generator.send(2)

        numerator, denominator = convergent.numerator, convergent.denominator

        if len(number_to_list(numerator)) > len(number_to_list(denominator)):
            count += 1

    return count
