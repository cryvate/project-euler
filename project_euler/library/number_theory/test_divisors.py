import pytest

from .divisors import divisor_count, divisor_sum


@pytest.mark.parametrize("n", range(1, 100))
def test_divisor_count(n: int) -> None:
    assert len([factor for factor in range(1, n + 1) if n % factor == 0]) == \
           divisor_count(n)


@pytest.mark.parametrize("n", range(1, 100))
def test_divisor_sum(n: int) -> None:
    assert sum([factor for factor in range(1, n + 1) if n % factor == 0]) == \
           divisor_sum(n)
