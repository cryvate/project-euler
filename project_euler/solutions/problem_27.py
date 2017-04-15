from itertools import count

from ..library.number_theory.primes import is_prime, prime_sieve


def consecutive(a: int, b: int, sieve) -> int:
    # assume b prime

    for n in count(1):
        if not is_prime(n ** 2 + a * n + b, sieve):
            return n


def solve(a_bound: int=1_000, b_bound: int=1_000, sieve_bound: int=10_00) -> int:
    maximum = 0
    result = 0

    primes = prime_sieve(sieve_bound)

    for a in range(-a_bound, a_bound + 1):
        for b in primes:
            present = consecutive(a, b, primes)

            if present > maximum:
                maximum = present
                result = a * b

    return result
