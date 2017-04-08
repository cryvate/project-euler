from ..library.number_theory.divisors import divisor_sum


def solve(bound: int=10000) -> int:
    proper_divisors = [0] + [divisor_sum(n) - n for n in range(1, bound)]

    return sum(n for n, divisors in enumerate(proper_divisors) if
               n != divisors and divisors < bound and
               proper_divisors[divisors] == n)
