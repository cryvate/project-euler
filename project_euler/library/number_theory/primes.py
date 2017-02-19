from math import sqrt, floor
from typing import Callable


def is_prime_trial_division(n: int) -> bool:
    if n <= 1:
        return False

    for factor in range(2, n):
        if n % factor == 0:
            return False

    return True


def is_prime_trial_division_sqrt(n: int) -> bool:
    if n <= 1:
        return False

    for factor in range(2, floor(sqrt(n)) + 1):
        if n % factor == 0:
            return False

        if factor * factor > n:
            return True

    return True


def prime_factor_trial_division_sqrt(n: int) -> int:
    if n <= 1:
        raise ZeroDivisionError

    for factor in range(2, floor(sqrt(n)) + 1):
        if n % factor == 0:
            return factor

        if factor * factor > n:
            return n

    return n


def is_prime_using_sieve(n: int, sieve: Callable[[int], bool]) -> bool:
    if n <= 1:
        return False

    if n < len(sieve):
        return sieve[n]

    permissible_factors = (factor for factor in range(2, sqrt(n))
                           if sieve[factor])

    for factor in permissible_factors:
        if n % factor == 0:
            return False

    return True


def prime_sieve(n: int) -> bool:
    """
    From here:

    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all
    -primes-below-n/3035188#3035188
    """
    import numpy

    if n <= 1:
        return [False] * n

    sieve = numpy.ones(n // 3 + (n % 6 == 2), dtype=numpy.bool)

    for i in range(1, int(sqrt(n)) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False

    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]
