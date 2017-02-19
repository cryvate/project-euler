import pytest

from .sqrt import csqrt, fsqrt


@pytest.mark.parametrize("n", (10 ** n for n in range(10)))
def test_sqrt(n):
    lower = fsqrt(n)
    upper = csqrt(n)

    assert upper - lower in (0, 1)
    assert lower ** 2 <= n <= upper ** 2
