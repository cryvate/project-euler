from typing import List

from .primes import generate_prime_factors, prime_sieve
from ..sqrt import csqrt


def phi(n: int) -> int:
    result = n

    for factor in generate_prime_factors(n):
        result *= (factor - 1)
        result //= factor

    return result


def phi_range(n: int) -> List[int]:
    import numpy as np

    phis = np.zeros(n + 1, dtype=np.int64)
    for i in range(n + 1):
        phis[i] = i

    primes = prime_sieve(csqrt(n))

    for prime in primes:
        phis[prime::prime] = (phis[prime::prime] * (prime - 1)) // prime

    for i in range(primes[-1] + 1, n + 1):
        if phis[i] == i:
            phis[i::i] = (phis[i::i] * (i - 1)) // i

    return phis.tolist()
