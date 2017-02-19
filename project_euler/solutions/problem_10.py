from ..library.number_theory.primes import prime_sieve


def solve(number: int=2_000_000) -> str:
    return str(sum(prime_sieve(number)))
