import os
from importlib import import_module

import pytest

from .convert import convert
from .solve import solve

problems = []
problems_with_solution = []
for filename in os.listdir(os.path.split(__file__)[0]):
    if filename.endswith(".py") and filename.startswith("problem_"):
        problem_number = int(filename[8:-3])
        problems.append(problem_number)

        problem_module = import_module(f'.problem_{problem_number}',
                                       package='project_euler.solutions')

        try:
            problem_module.answer_b64
            problems_with_solution.append(problem_number)
        except AttributeError:
            pass


@pytest.mark.parametrize("problem_number", problems_with_solution)
def test_answer(problem_number: int):
    problem_module = import_module(f'.problem_{problem_number}',
                                   package='project_euler.solutions')

    assert convert(solve(problem_number)) == problem_module.answer_b64


@pytest.mark.parametrize("problem_number", problems)
def test_metadata_problems(problem_number: int):
    problem_module = import_module(f'.problem_{problem_number}',
                                   package='project_euler.solutions')

    try:
        problem_module.title
    except AttributeError as e:
        raise ProblemMalformedException(f'No title in problem '
                                        f'{problem_number}.') from e

    try:
        problem_module.description
    except AttributeError as e:
        raise ProblemMalformedException(f'No description in problem '
                                        f'{problem_number}.') from e

    try:
        if problem_number in problems_with_solution:
            problem_module.strategy
    except AttributeError as e:
        raise ProblemMalformedException(f'No strategy in problem '
                                        f'{problem_number} while providing '
                                        f'answer.'
                                        f'') from e


class ProblemMalformedException(Exception):
    pass
