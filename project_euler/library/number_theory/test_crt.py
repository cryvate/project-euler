from itertools import product

import pytest

from .crt import crt


@pytest.mark.parametrize('a,m,b,n', product(*([list(range(100, 105))] *
                                              4)))
def test_crt(a: int, m: int, b: int, n: int) -> None:
    try:
        answer = crt(a, m, b, n)
        assert answer % m == a % m
        assert answer % n == b % n
    except ValueError:
        return
        assert len([x for x in range(0, m * n) if x % m == a and x % n ==
                    b]) == 0
