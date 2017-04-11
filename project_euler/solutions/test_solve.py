import pytest

from .solve import solve, SolveException


def test_solve_valid_problem():
    solve(2)


def test_solve_invalid_problem():
    with pytest.raises(SolveException):
        solve('Here be dragons...')
