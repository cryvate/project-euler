from itertools import count

from ..library.number_theory.continued_fractions import convergent_sequence
from ..library.base import number_to_list


def solve(index: int=100) -> int:
    def as_e():
        yield 2

        for i in count(2, 2):
            yield 1
            yield i
            yield 1

    convergents = convergent_sequence(as_e())

    for convergent, _ in zip(convergents, range(index)):
        pass

    return sum(number_to_list(convergent.numerator))