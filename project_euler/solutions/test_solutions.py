import pytest

from project_euler.framework.solve import solve_problem
from .problems import numbers as problems


test_problem = \
    pytest.mark.parametrize('problem_number', problems)(solve_problem)
