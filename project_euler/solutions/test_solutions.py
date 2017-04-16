import pytest

from .problems import numbers as problems

from .solve import solve_problem


test_problem = \
    pytest.mark.parametrize('problem_number', problems)(solve_problem)
