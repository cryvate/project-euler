#!/usr/bin/env python

"""Solver for Project Euler problems.

Usage:
    solve <problem_number>
    solve (-h | --help)

Options:
    -h --help  Show this screen.

"""

from importlib import import_module
from os.path import join, split
import time
import warnings

from typing import Any, Callable, Tuple

from docopt import docopt
import yaml

import project_euler.solutions  # noqa: F401
from project_euler.solutions.problems import slow_numbers as slow_problems

spec = '{:4.2f}'

MINUTE_RULE = 60
SLOW = 10


class SolveException(Exception):
    pass


class ProblemMalformed(SolveException):
    pass


class SolutionWrong(SolveException):
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


class AnswerVerificationFailed(SolutionWrong):
    pass


class OneMinuteRuleViolation(SolutionWrong):
    pass


def solve_problem(problem_number: int,
                  solve: Callable[[], Any]=None,
                  minute_rule: float=None,
                  slow: float=None) -> Tuple[str, float]:
    if not minute_rule:
        minute_rule = MINUTE_RULE
    if not slow:
        slow = SLOW

    file_name = f'problem_{problem_number}.yaml'

    file_path = join(join(split(__file__)[0], '..', 'solutions', file_name))

    with open(file_path) as f:
        parameters = yaml.load(f)

    parameters['title']
    parameters['description']
    reference_answer = parameters['answer_b64'].decode()
    parameters['strategy']

    if not solve:
        problem_module = import_module(f'.problem_{problem_number}',
                                       package='project_euler.solutions')
        solve = problem_module.solve

    start = time.time()

    answer = str(solve())
    # often more natural to return int

    spent = time.time() - start

    kwargs = {
        'answer': answer,
        'reference_answer': reference_answer,
        'spent': spent
    }

    reference_answer = parameters['answer_b64'].decode()

    if answer != reference_answer:
        raise AnswerVerificationFailed(
            f'In problem {problem_number} the calculated answer is '
            f'{answer} ({spec.format(spent)}s), the reference answer is '
            f'{reference_answer}.', **kwargs)

    print(f'Problem {problem_number} took {spec.format(spent)}s and the '
          f'answer {answer} was correct.')

    if spent > minute_rule:
        if problem_number in slow_problems:
            slower_time = slow_problems[problem_number]
            if spent > slower_time:
                raise OneMinuteRuleViolation(
                    f'Problem {problem_number} took {spec.format(spent)}s,'
                    f' which is more than the {slower_time}s it is '
                    f'allowed to take.', **kwargs)
            else:
                warnings.warn(
                    f'Problem {problem_number} took {spec.format(spent)}s,'
                    f' which is less than the {slower_time}s it is allowed'
                    f' to take, but more than {minute_rule}s.',
                    UserWarning)
        else:
            raise OneMinuteRuleViolation(
                f'Problem {problem_number} took {spec.format(spent)}s, '
                f'which is more than a minute!', **kwargs)
    elif spent > slow:
        warnings.warn(
                    f'Problem {problem_number} took {spec.format(spent)}s,'
                    f' which is more than {slow}s.', UserWarning)

    return answer, spent


if __name__ == '__main__':
    arguments = docopt(__doc__)

    problem_number = arguments['<problem_number>']

    solve_problem(problem_number)
