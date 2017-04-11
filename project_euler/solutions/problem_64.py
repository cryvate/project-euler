from ..library.number_theory.continued_fractions import continued_fraction_sqrt
from ..library.sqrt import is_square


def solve(bound: int=10_000) -> int:
    return sum(len(continued_fraction_sqrt(n)[1]) % 2
               for n in range(1, bound + 1) if not is_square(n))
