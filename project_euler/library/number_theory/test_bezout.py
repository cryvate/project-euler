from itertools import product

import pytest

from .bezout import bezout
from .gcd import gcd


@pytest.mark.parametrize('a,b', product(*([list(range(10, 15))] * 2)))
def test_bezout(a: int, b: int) -> None:
    x, y = bezout(a, b)

    assert x * a + y * b == gcd(a, b)
