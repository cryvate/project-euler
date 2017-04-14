from typing import List


from ..library.sqrt import fsqrt
from ..library.number_theory.primes import is_prime, prime_sieve


def is_circular_prime(n: int, sieve: List[int]) -> bool:
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[i:] + str(n)[:i]), sieve):
            return False

    print(n)

    return True


def solve(digits: int=6) -> int:
    maximum = 10 ** digits
    sieve = prime_sieve(fsqrt(maximum))

    return sum(1 for prime in range(maximum) if is_circular_prime(prime, sieve))
