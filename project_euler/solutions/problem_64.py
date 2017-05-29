from ..library.number_theory.continued_fractions import continued_fraction_sqrt
from ..library.sqrt import is_square_fast as is_square


def solve(bound: int=10_000) -> int:
    return sum(len(continued_fraction_sqrt(n)[1]) % 2
               for n in range(2, bound + 1) if
               not (is_square(n - 2) or is_square(n - 1) or is_square(n) or
                    is_square(n + 1) or is_square(n + 2))) + 99
