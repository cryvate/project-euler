import pytest

from .divisors import divisor_count, divisor_sum, divisor_range


@pytest.mark.parametrize("n", range(1, 100))
def test_divisor_count(n: int) -> None:
    assert len([factor for factor in range(1, n + 1) if n % factor == 0]) == \
           divisor_count(n)


@pytest.mark.parametrize("n", range(1, 100))
def test_divisor_sum(n: int) -> None:
    assert sum([factor for factor in range(1, n + 1) if n % factor == 0]) == \
           divisor_sum(n)


def test_divisor_range(n: int=100) -> None:
    assert divisor_range(n)[1:] == [divisor_sum(n) for n in range(1, n + 1)]
