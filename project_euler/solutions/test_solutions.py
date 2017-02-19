import os
import time

import pytest
import yaml

from .problems import numbers
from .solve import solve

problems = numbers


@pytest.mark.parametrize("problem_number", problems)
def test_yaml_problems(problem_number: int):
    filename = os.path.join(os.path.split(__file__)[0], f'problem_'
                                                        f'{problem_number}'
                                                        f'.yaml')
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
        start = time.time()
        answer = solve(problem_number)
        spent = time.time() - start

        if spent > 60:
            raise OneMinuteRuleViolation(f"Problem {problem_number} took "
                                         f"{spent} seconds, which is more "
                                         f"than a minute!")

        reference_answer = parameters['answer_b64'].decode()

        if answer != reference_answer:
            raise AnswerVerifcationFailed(f'In problem {problem_number} the '
                                          f'calculated answer is {answer} '
                                          f'whereas the reference answer is '
                                          f'{reference_answer}.')


class ProblemMalformed(Exception):
    pass


class OneMinuteRuleViolation(Exception):
    pass


class AnswerVerifcationFailed(Exception):
    pass
