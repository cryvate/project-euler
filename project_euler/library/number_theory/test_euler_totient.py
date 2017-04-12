import pytest

from .euler_totient import phi, phi_range
from .gcd import gcd


@pytest.mark.parametrize('n', range(100, 115))
def test_phi(n: int) -> None:
    assert phi(n) == len([a for a in range(n) if gcd(a, n) == 1])


def test_phi_range(n: int=100):
    assert [phi(n) for n in range(1, n + 1)] == phi_range(n)[1:]
