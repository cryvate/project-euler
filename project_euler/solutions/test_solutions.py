import os
import time

import pytest
import yaml

from .problems import numbers as problems
from .solve import solve


class OneMinuteRuleViolation(Exception):
    pass


@pytest.mark.xfail(condition='problem_number == 66',
                   reason='Problem takes ~30s on normal hardware, Travis is '\
                          'too slow and goes over 60s',
                   raises=OneMinuteRuleViolation,
                   run=True,
                   strict=False)
@pytest.mark.parametrize('problem_number', problems)
def test_yaml_problems(problem_number: int) -> str:
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

        start = time.time()
        answer = str(solve(problem_number))  # often more natural to return int
        spent = time.time() - start

        if spent > 60:
            raise OneMinuteRuleViolation(f'Problem {problem_number} took '
                                         f'{round(spent, 2)} seconds, which '
                                         f'is more than a minute!')

        reference_answer = parameters['answer_b64'].decode()

        if answer != reference_answer:
            raise AnswerVerifcationFailed(f'In problem {problem_number} the '
                                          f'calculated answer is {answer} '
                                          f'whereas the reference answer is '
                                          f'{reference_answer}.',
                                          answer=answer,
                                          reference_answer=reference_answer,
                                          spent=spent)

    return answer, spent


class ProblemMalformed(Exception):
    pass


class AnswerVerifcationFailed(Exception):
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
