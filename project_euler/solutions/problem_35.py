from typing import List


from ..library.number_theory.primes import prime_sieve


def is_circular_prime(n: int, sieve: List[int]) -> bool:
    # assume prime

    for i in range(1, len(str(n))):
        if int(str(n)[i:] + str(n)[:i]) not in sieve:
            return False

    return True


def solve(digits: int=6) -> int:
    sieve = prime_sieve(10 ** digits)

    return sum(1 for prime in sieve if is_circular_prime(prime, sieve))
