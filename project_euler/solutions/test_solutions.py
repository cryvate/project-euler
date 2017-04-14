import os
import time
import warnings

import pytest
import yaml

from .problems import numbers as problems, slow_numbers as slow_problems


@pytest.mark.parametrize('problem_number', problems)
def test_problems(problem_number: int) -> str:
    from .solve import solve, ProblemMalformed, OneMinuteRuleViolation, \
        AnswerVerificationFailed
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

        spec = '{:4.2f}'

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

        reference_answer = parameters['answer_b64'].decode()

        if answer != reference_answer:
            raise AnswerVerificationFailed(
                f'In problem {problem_number} the calculated answer is '
                f'{answer} ({spec.format(spent)}s), the reference answer is '
                f'{reference_answer}.', **kwargs)

    return answer, spent
