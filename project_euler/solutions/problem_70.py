from fractions import Fraction

from ..library.number_theory.primes import is_prime
from ..library.base import is_permutation
from ..library.sqrt import csqrt


def solve(bound: int=10_000_000) -> int:
    primes = []

    middle = csqrt(bound)
    around = 10 * csqrt(middle)

    for i in range(1, middle + around):
        if is_prime(i):
            primes.append(i)

    maximum = (Fraction(2, 1), 2)

    for i, p in enumerate(primes):
        if p > middle:
            break
        for q in primes[i:]:
            if p * q > bound:
                break
            if is_permutation(p * q, (p - 1) * (q - 1)):
                maximum = min(maximum, (Fraction(p * q, (p - 1) * (q - 1)),
                                        p * q))

    return maximum[1]
