from time import sleep

from typing import Callable

import pytest

from .solve import solve_problem, AnswerVerificationFailed, \
    OneMinuteRuleViolation


def raise_exception(exception: BaseException) -> Callable[[], None]:
    def function():
        raise exception()

    return function


INVALID_KINDS = [
    (
        1,
        lambda: 0,
        AnswerVerificationFailed
    ),
    (
        1,
        lambda: sleep(0.02) or 233168,
        OneMinuteRuleViolation
    ),
    (
        '1',
        lambda: sleep(0.01) or 233168,
        UserWarning
    ),
    (
        '1',
        lambda: sleep(0.02) or 233168,
        UserWarning
    ),
    (
        '1',
        lambda: sleep(0.03) or 233168,
        OneMinuteRuleViolation
    ),
    (
        '1',
        raise_exception(ValueError),
        ValueError
    )
]


def test_solve_valid_problem():
    solve_problem(1)


@pytest.mark.parametrize('kind,solve,exception', INVALID_KINDS)
def test_solve_invalid_data(kind, solve, exception):
    with pytest.raises(exception) if not issubclass(exception, Warning) else \
            pytest.warns(exception):
        solve_problem(kind, solve, 0.02, 0.01)
