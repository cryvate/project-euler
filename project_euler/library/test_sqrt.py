from math import sqrt

import pytest

from .sqrt import fsqrt, csqrt


@pytest.mark.parametrize('n', range(100, 1000))
def test_sqrt(n: int) -> None:
    assert max(x for x in range(n) if x * x <= n) == fsqrt(n)
    assert min(x for x in range(n) if x * x >= n) == csqrt(n)
