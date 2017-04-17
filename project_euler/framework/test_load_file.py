from os.path import join, split

from .solve import solve_problem
from ..solutions.problem_22 import solve


def test_load_file() -> None:
    answer, _ = solve_problem(22)

    directory = join(split(__file__)[0], '..', 'data', 'problems')

    assert answer == \
        str(solve(join(directory, '22_names.txt'), False))
