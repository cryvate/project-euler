import pytest

from .euler_totient import phi
from .gcd import gcd


@pytest.mark.parametrize('n', range(100, 115))
def test_phi(n: int) -> None:
    assert phi(n) == len([a for a in range(n) if gcd(a, n) == 1])
