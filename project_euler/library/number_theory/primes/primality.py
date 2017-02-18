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

    for factor in range(2, floor(sqrt(n))):
        if n % factor == 0:
            return False

        if factor * factor >= n:
            return True

    return True


def is_prime_using_sieve(n: int, sieve: Callable[int, bool]) -> bool:
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
