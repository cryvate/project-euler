from collections import OrderedDict

import pytest

from .convert import convert
from .solve import solve

solutions_hashed = OrderedDict()
# To add a solution, run "convert <answer>" and add below.

# The below is bae64-encoded to leave it spoiler-free.
# The answers can be found by Googling, so more 'security' is not required.
solutions_hashed[1] = b'MjMzMTY4\n'


@pytest.mark.parametrize("problem_number", (x for x in solutions_hashed))
def test_problem_1(problem_number):
    assert convert(solve(problem_number)) == solutions_hashed[1]
