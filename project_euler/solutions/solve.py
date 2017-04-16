#!/usr/bin/env python

'''Solver for Project Euler problems.

Usage:
    solve <problem_number>
    solve (-h | --help)

Options:
    -h --help  Show this screen.

'''

from importlib import import_module
import os
import time
import warnings

from docopt import docopt
import yaml

import project_euler.solutions  # noqa: F401
from project_euler.solutions.problems import slow_numbers as slow_problems

spec = '{:4.2f}'


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


def solve_problem(problem_number: int) -> str:

    filename = os.path.join(os.path.split(__file__)[0],
                            f'problem_{problem_number}.yaml')
    try:
        with open(filename) as f:
            parameters = yaml.load(f)
    except FileNotFoundError as e:
        raise ProblemMalformed(f'File problem_{problem_number}.yaml not '
                               f'found.') from e

    if "title" not in parameters:
        raise ProblemMalformed(f'No title in problem {problem_number}.')
    if "description" not in parameters:
        raise ProblemMalformed(f'No description in problem {problem_number}.')

    if "answer_b64" in parameters:
        if "strategy" not in parameters:
            raise ProblemMalformed(f'No strategy in problem {problem_number} '
                                   f'while providing answer.')

        reference_answer = parameters['answer_b64'].decode()

        start = time.time()
        answer = str(solve(problem_number))  # often more natural to return int
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

        if spent > 60:
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
                        f' to take, but more than 60s',
                        UserWarning)
            else:
                raise OneMinuteRuleViolation(
                    f'Problem {problem_number} took {spec.format(spent)}s, '
                    f'which is more than a minute!', **kwargs)

    return answer, spent


def solve(problem_number: int) -> str:
    try:
        problem_module = import_module(f'.problem_{problem_number}',
                                       package='project_euler.solutions')
    except ModuleNotFoundError as e:
        raise SolveException(f"The problem {problem_number} does not seem to "
                             "have a solution in this package.") from e

    return problem_module.solve()


if __name__ == '__main__':
    arguments = docopt(__doc__)

    problem_number = arguments['<problem_number>']

    solve_problem(problem_number)
