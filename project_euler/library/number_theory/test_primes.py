import pytest

from ..test_series import reference_values
from .primes import is_prime, is_prime_using_sieve, largest_prime_factor,\
    prime_sieve, smallest_prime_factor

primes_list = reference_values["primes"]


@pytest.mark.parametrize("n", range(-100, max(primes_list) + 1))
def test_is_prime(n: int):
    assert is_prime(n) == (n in primes_list)


@pytest.mark.parametrize("n", range(-100, 2))
def test_smallest_prime_factor_negative_error(n):
    with pytest.raises(ValueError):
        smallest_prime_factor(n)


@pytest.mark.parametrize("p,remainder", ((2, 1), (2, 5), (5, 77)))
def test_smallest_prime_factor(p: int, remainder: int):
    assert smallest_prime_factor(p * remainder) == p


@pytest.mark.parametrize("n", range(-100, 2))
def test_largest_prime_factor_negative_error(n):
    with pytest.raises(ValueError):
        smallest_prime_factor(n)


@pytest.mark.parametrize("p,remainder", ((2, 1), (5, 2), (11, 35)))
def test_largest_prime_factor(p: int, remainder: int):
    assert largest_prime_factor(p * remainder) == p


def test_sieve():
    n = max(primes_list)

    assert list(prime_sieve(n + 1)) == primes_list


def test_is_prime_using_sieve():
    n = max(primes_list)

    sieve = prime_sieve(n + 1)

    primes = prime_sieve(n * n)

    for p in range(n * n):
        assert is_prime_using_sieve(p, sieve) == (p in primes)
