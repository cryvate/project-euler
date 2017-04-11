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

from project_euler.solutions.test_solutions import test_problems

import project_euler.solutions  # noqa: F401


def solve(problem_number: int) -> str:
    try:
        problem_module = import_module(f'.problem_{problem_number}',
                                       package='project_euler.solutions')
    except ModuleNotFoundError as e:
        raise SolveException(f"The problem {problem_number} does not seem to "
                             "have a solution in this package.") from e

    return problem_module.solve()


class SolutionWrong(Exception):
    def __init__(self,
                 *args,
                 answer: str,
                 reference_answer: str,
                 spent: float,
                 **kwargs):
        self.answer = answer
        self.reference_answer = reference_answer
        self.spent = spent

        super().__init__(*args, **kwargs)


class ProblemMalformed(Exception):
    pass


class AnswerVerificationFailed(SolutionWrong):
    pass


class OneMinuteRuleViolation(SolutionWrong):
    pass


class SolveException(Exception):
    pass


if __name__ == '__main__':
    arguments = docopt(__doc__)

    problem_number = arguments['<problem_number>']

    spec = '{:6.4f}'

    try:
        result, spent = test_problems(problem_number)
    except SolutionWrong as e:
        print(f'Implemented answer: {e.answer} (in {spec.format(e.spent)}s)')
        print(f'Reference solution: {e.reference_answer}')
        print(f'This does *NOT* agree with reference answer.')
    else:
        print(f'Solution: {result} (in {spec.format(spent)}s)')
        print('This *does* agree with reference answer.')
