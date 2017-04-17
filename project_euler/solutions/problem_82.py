from .problem_81 import solve as solve_matrix


def solve(name: str='matrix.txt', relative: bool=True) -> int:
    return solve_matrix(name,
                        relative,
                        ((-1, 0), (0, 1), (1, 0)),
                        sources=[(i, 0) for i in range(80)],
                        drains=[(i, -1) for i in range(80)])
