from typing import Tuple


def solve(bound: int=1000, divisors: Tuple[int, int]=(3, 5)) -> int:
    counter = 0

    for divisor in divisors:
        counter += sum(range(0, bound, divisor))

    counter -= sum(range(0, bound, divisors[0] * divisors[1]))

    return counter
