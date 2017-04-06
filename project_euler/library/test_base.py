import pytest

from typing import List

from .base import number_to_list, list_to_number


NUMBER_TO_LIST = [(2, [2], 10), (12, [1, 2], 10), (6, [2, 0], 3)]


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
