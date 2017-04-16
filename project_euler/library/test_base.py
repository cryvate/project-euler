import pytest

from typing import List, Tuple

from .base import number_to_list, list_to_number, is_permutation, \
    range_combinations_digits, count_combinations_digits, count_permutations


NUMBER_TO_LIST = [(2, [2], 10), (12, [1, 2], 10), (6, [2, 0], 3)]

PERMUTATIONS = [
    (15, 51, 10, True),
    (2, 3, 10, False),
    (12, 10, 2, True),
    (4, 3, 2, False),
    (15, 5000, 10, False),
]

RANGE_COMBINATIONS = [
    (
        [0, 2],
        [()] + [(i,) for i in range(1, 10)]
    )
]

COUNT_COMBINATIONS = [
    (
        [1],
        8,
        [(i,) for i in range(1, 8)]
    )
]

COMBINATION_CONTRIBUTIONS = [
    (
        [1, 2, 3, 3],
        True,
        21
    )
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


@pytest.mark.parametrize('args,expected_output', RANGE_COMBINATIONS)
def test_range_combinations_digits(args, expected_output) -> None:
    assert list(range_combinations_digits(*args)) == expected_output


@pytest.mark.parametrize('args,max_value,expected_output', COUNT_COMBINATIONS)
def test_count_combinations_digits(args: List[int],
                                   max_value: int,
                                   expected_output: List[Tuple[int]]) -> None:
    result = []
    for value in count_combinations_digits(*args):
        print(value)
        if list_to_number(value) >= max_value:
            break

        result.append(value)

    assert result == expected_output


@pytest.mark.parametrize('combination,one_also_zero_not_leading,contribution',
                         COMBINATION_CONTRIBUTIONS)
def test_count_permutations(combination: Tuple[int],
                            one_also_zero_not_leading: bool,
                            contribution: int) -> None:
    assert count_permutations(combination, one_also_zero_not_leading) == \
           contribution
