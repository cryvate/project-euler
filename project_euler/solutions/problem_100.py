from ..library.number_theory.pells_equation import \
    solve_negative_pells_equation


def solve(bound: int=1_000_000_000_000):
    for x, y in solve_negative_pells_equation(2):
        total = (x + 1) // 2
        blue = (y + 1) // 2

        if total > bound:
            return blue
