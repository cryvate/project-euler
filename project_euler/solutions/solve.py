#!/usr/bin/env python

'''Solver for Project Euler problems.

Usage:
    solve <problem_number>
    solve (-h | --help)

Options:
    -h --help  Show this screen.

'''

import os
from importlib import import_module

from docopt import docopt

import project_euler.solutions  # noqa: F401


def solve(problem_number: int, verbose: bool=False) -> str:
    try:
        problem_module = import_module(f'.problem_{problem_number}',
                                       package='project_euler.solutions')
    except ModuleNotFoundError as e:
        raise SolveException("This problem does not seem to have a solution"
                             "provided by this package.") from e

    if verbose:
        _, columns = os.popen('stty size', 'r').read().split()
        columns = int(columns)
        print("=" * columns)
        print(f'Solving Project Euler problem {problem_number}:'
              f'{problem_module.title}')
        print("=" * columns)
        print("DESCRIPTION")
        print("=" * columns)
        print(problem_module.description)
        print("=" * columns)
        print("STRATEGY")
        print("=" * columns)
        print(problem_module.strategy)

    print(problem_module.solve())

    return problem_module.solve()


class SolveException(Exception):
    pass


if __name__ == '__main__':
    arguments = docopt(__doc__)

    problem_number = arguments['<problem_number>']

    solve(problem_number, True)
