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
from termcolor import colored  # noqa: F401
import yaml

import project_euler.solutions  # noqa: F401
from project_euler.solutions.problems import slow_numbers as slow_problems

spec = '{:4.2f}'

MINUTE_RULE = 60
SLOW = 10


SOLVE_MSG = ('{colored("[PE-" + str(problem_number) +"]", status_colour)} '
             '{colored(str(answer), "green") if answer_correct else colored(str(answer) + " != " + str(reference_answer), "red")} '  # noqa: E501
             '{colored("[" + spec.format(spent) + "s" + "!" * (minute_violated + slow_violated) + "]", "green" if spent <= slow else ("yellow" if spent <= minute_rule else "red"))}')  # noqa: E501
SOLVE_MSG_E = ''


class SolveException(Exception):
    pass


class ProblemMalformed(SolveException):
    pass


class SolutionWrong(SolveException):
    pass


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

    file_path = join(join(split(__file__)[0], '..', 'problems', file_name))

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

    reference_answer = parameters['answer_b64'].decode()

    start = time.time()

    try:
        answer = str(solve())
        # often more natural to return int
    except Exception as e:
        answer = str(type(e))[8:-2] + "_occured"

        spent = time.time() - start

        answer_correct = answer == reference_answer
        minute_violated = spent > minute_rule
        slow_violated = spent > slow
        status_colour_time = 'green' if slow_violated else (  # NOQA: F841
            'yellow' if minute_violated else 'red')
        status_colour = 'green' if answer_correct and not slow_violated else (  # noqa: F841,E501
            'yellow' if answer_correct and not minute_violated else 'red')

        print(eval('f' + repr(SOLVE_MSG)))

        raise

    spent = time.time() - start

    answer_correct = answer == reference_answer
    minute_violated = spent > minute_rule
    slow_violated = spent > slow
    status_colour_time = 'green' if slow_violated else (  # NOQA: F841
        'yellow' if minute_violated else 'red')
    status_colour = 'green' if answer_correct and not slow_violated else (  # noqa: F841,E501
        'yellow' if answer_correct and not minute_violated else 'red')

    print(eval('f' + repr(SOLVE_MSG)))

    if not answer_correct:
        raise AnswerVerificationFailed(
            f'In problem {problem_number} the calculated answer is '
            f'{answer} ({spec.format(spent)}s), the reference answer is '
            f'{reference_answer}.')

    if minute_violated:
        if problem_number in slow_problems:
            slower_time = slow_problems[problem_number]
            if spent > slower_time:
                raise OneMinuteRuleViolation(
                    f'Problem {problem_number} took {spec.format(spent)}s,'
                    f' which is more than the {slower_time}s it is '
                    f'allowed to take.')
            else:
                warnings.warn(
                    f'Problem {problem_number} took {spec.format(spent)}s,'
                    f' which is less than the {slower_time}s it is allowed'
                    f' to take, but more than {minute_rule}s.',
                    UserWarning)
        else:
            raise OneMinuteRuleViolation(
                f'Problem {problem_number} took {spec.format(spent)}s, '
                f'which is more than a minute!')
    elif slow_violated:
        warnings.warn(
                    f'Problem {problem_number} took {spec.format(spent)}s,'
                    f' which is more than {slow}s.', UserWarning)

    return answer, spent


if __name__ == '__main__':
    arguments = docopt(__doc__)

    problem_number = arguments['<problem_number>']

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            solve_problem(problem_number)
    except SolveException:
        pass
