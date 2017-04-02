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
        raise SolveException(f"This problem {problem_number} does not seem to "
                             "have a solution in this package.") from e

    return problem_module.solve()


class SolveException(Exception):
    pass


if __name__ == '__main__':
    arguments = docopt(__doc__)

    problem_number = arguments['<problem_number>']

    print(solve(problem_number))
