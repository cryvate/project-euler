import pytest

from .palindrome import is_palindrome

TEST_CASES = [
    (101, 10, True),
    (11, 10, True),
    (7, 2, True),
    (123, 10, False),
    (4, 2, False),
    (0, 2, False),
]


@pytest.mark.parametrize('n,base,expected_output', TEST_CASES)
def test_is_palindrome(n: int, base: int, expected_output: bool):
    assert is_palindrome(n, base) == expected_output
