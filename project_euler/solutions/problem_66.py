from ..library.number_theory.pells_equation import solve_pells_equation
from ..library.sqrt import is_square

def solve(bound: int=1_000) -> int:
    return max((next(solve_pells_equation(n))[0], n)
               for n in range(1, bound + 1) if not is_square(n))[1]
