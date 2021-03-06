from itertools import count

from ..library.number_theory.divisors import divisor_count


def solve(over: int=500) -> int:
    for n in count(1):
        if n % 2 == 0:
            no_divisors = divisor_count(n // 2) * divisor_count(n + 1)
        else:
            no_divisors = divisor_count(n) * divisor_count((n + 1) // 2)

        if no_divisors > over:
            return (n * (n + 1)) // 2

    raise RuntimeError('This code is unreachable.')
