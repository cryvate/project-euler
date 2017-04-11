import pytest

from typing import Tuple

from .pells_equation import solve_pells_equation
from ..sqrt import is_square


PELLS_SOLUTIONS = [
    (
        2,
        [
            3,
            2
        ]
    ),
    (
        3,
        [
            2,
            1
        ]
    ),
    (
        5,
        [
            9,
            4
        ]
    ),
    (
        6,
        [
            5,
            2
        ]
    ),
    (
        7,
        [
            8,
            3
        ]
    ),
]

RANGE = [n for n in range(1, 20) if not is_square(n)]
DEPTH = 100


@pytest.mark.parametrize('n,expected_output', PELLS_SOLUTIONS)
def test_first_solution_pells_equation(n: int,
                                       expected_output: Tuple[int, int]) -> \
        None:
    assert tuple(expected_output) == next(solve_pells_equation(n))


@pytest.mark.parametrize('n', RANGE)
def test_further_solutions_pells_equation(n: int,
                                          number: int=DEPTH) -> None:
    solutions = solve_pells_equation(n)

    for (x, y), i in zip(solutions, range(number)):
        assert x ** 2 - n * y ** 2 == 1
