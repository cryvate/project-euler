from ..library.number_theory.primes import prime_sieve


def solve(number: int=2_000_000) -> int:
    return sum(prime_sieve(number))
