from .problem_81 import solve as solve_matrix


def solve(name: str='matrix.txt', relative: bool=True) -> int:
    return solve_matrix(name,
                        relative,
                        ((-1, 0), (0, -1), (0, 1), (1, 0)))
