from ..sqrt import fsqrt
from typing import Sequence


def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    for factor in range(2, fsqrt(n) + 1):
        if n % factor == 0:
            return False

    return True


def smallest_prime_factor(n: int) -> int:
    if n <= 1:
        raise ValueError

    for factor in range(2, fsqrt(n) + 1):
        if n % factor == 0:
            return factor

    return n


def largest_prime_factor(n: int) -> int:
    if n <= 1:
        raise ValueError

    bound = fsqrt(n) + 1
    factor = 2

    while factor <= bound:
        if n % factor == 0:
            while n % factor == 0:
                n //= factor

            if n == 1:
                return factor

            bound = fsqrt(n) + 1

        factor += 1

    return n


def is_prime_using_sieve(n: int, sieve: Sequence[int]) -> bool:
    if n <= 1:
        return False

    if n in sieve:
        return True

    permissible_factors = (factor for factor in range(2, fsqrt(n) + 1)
                           if factor in sieve)

    for factor in permissible_factors:
        if n % factor == 0:
            return False

    return True


def prime_sieve(n: int) -> Sequence[int]:
    """
    From here:

    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all
    -primes-below-n/3035188#3035188
    """
    import numpy

    if n <= 1:
        return [False] * n

    sieve = numpy.ones(n // 3 + (n % 6 == 2), dtype=numpy.bool)

    for i in range(1, fsqrt(n) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False

    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]
