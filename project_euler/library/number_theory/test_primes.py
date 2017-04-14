import pytest

from ..test_sequences import reference_values
from .primes import is_prime, largest_prime_factor,\
    prime_sieve, smallest_prime_factor, generate_prime_factors_multiplicity

primes_list = reference_values["primes"]


@pytest.mark.parametrize("n", range(-1, max(primes_list) + 1))
def test_is_prime(n: int) -> None:
    assert is_prime(n) == (n in primes_list)
    assert is_prime(n, [2, 3, 5]) == (n in primes_list)


@pytest.mark.parametrize("n", range(-100, 2))
def test_smallest_prime_factor_negative_error(n) -> None:
    with pytest.raises(ValueError):
        smallest_prime_factor(n)


@pytest.mark.parametrize("p,remainder", ((2, 1), (2, 5), (5, 77)))
def test_smallest_prime_factor(p: int, remainder: int) -> None:
    assert smallest_prime_factor(p * remainder) == p


@pytest.mark.parametrize("n", range(-100, 2))
def test_largest_prime_factor_negative_error(n):
    with pytest.raises(ValueError):
        largest_prime_factor(n)


@pytest.mark.parametrize("p,remainder", ((2, 1), (5, 2), (11, 35)))
def test_largest_prime_factor(p: int, remainder: int) -> None:
    assert largest_prime_factor(p * remainder) == p


@pytest.mark.parametrize("n", range(1, 100))
def test_generate_prime_factors_multiplicity(n: int) -> None:
    for factor, multiplicity in generate_prime_factors_multiplicity(n):
        contribution = factor ** multiplicity

        assert n % contribution == 0

        n //= contribution

    assert n == 1


def test_sieve():
    assert len(list(prime_sieve(-1))) == 0

    n = max(primes_list)

    assert prime_sieve(0) == []

    assert list(prime_sieve(n + 1)) == primes_list
