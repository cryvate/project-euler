#!/usr/bin/env python

'''Solver for Project Euler problems.

Usage:
    solve <problem_number>
    solve (-h | --help)

Options:
    -h --help  Show this screen.

'''

from importlib import import_module

from docopt import docopt

import project_euler.solutions  # noqa: F401


def solve(problem_number: int) -> str:
    try:
        problem_module = import_module(f'.problem_{problem_number}',
                                       package='project_euler.solutions')
    except ModuleNotFoundError as e:
        raise SolveException(f"The problem {problem_number} does not seem to "
                             "have a solution in this package.") from e

    return problem_module.solve()


class SolveException(Exception):
    pass


if __name__ == '__main__':
    arguments = docopt(__doc__)

    problem_number = arguments['<problem_number>']

    solution = solve(problem_number)

    print(f'Solution: {solution}')

    from project_euler.solutions.test_solutions import \
        AnswerVerifcationFailed, test_yaml_problems

    try:
        test_yaml_problems(problem_number)
    except AnswerVerifcationFailed:
        print(f'This does *NOT* agree with reference answer.')
    else:
        print(f'This *does* agree with reference answer.')
