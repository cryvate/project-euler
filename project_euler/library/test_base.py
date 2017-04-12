import pytest

from typing import List

from .base import number_to_list, list_to_number, is_permutation


NUMBER_TO_LIST = [(2, [2], 10), (12, [1, 2], 10), (6, [2, 0], 3)]

PERMUTATIONS = [
    (15, 51, 10, True),
    (2, 3, 10, False),
    (12, 10, 2, True),
    (4, 3, 2, False),
    (15, 5000, 10, False),
]


@pytest.mark.parametrize('number,expected_output,base', NUMBER_TO_LIST)
def test_number_to_list(number: int,
                        expected_output: int,
                        base: int) -> None:
    assert number_to_list(number, base)


@pytest.mark.parametrize('expected_output,representation,base', NUMBER_TO_LIST)
def test_list_to_number(representation: List[int],
                        expected_output: int,
                        base: int) -> None:
    assert list_to_number(representation, base) == expected_output


@pytest.mark.parametrize('self,other,base,expected_output', PERMUTATIONS)
def test_is_permutation(self: int,
                        other: int,
                        base: int,
                        expected_output: bool) -> None:
    assert is_permutation(self, other, base) == expected_output
