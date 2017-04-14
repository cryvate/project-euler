from bisect import bisect_right
from itertools import chain, count

from typing import Generator, Sequence, Tuple

from ..sqrt import fsqrt


def is_prime(n: int, sieve: Sequence[int]=None) -> bool:
    if n <= 1:
        return False

    if sieve is None:
        for factor in range(2, fsqrt(n) + 1):
            if n % factor == 0:
                return False
    elif n <= sieve[-1]:
        index = bisect_right(sieve, n)
        if not index or sieve[index - 1] != n:
            return False
    elif n <= sieve[-1] ** 2:
        for factor in sieve:
            if n % factor == 0:
                return False
    else:
        for factor in chain(sieve, range(sieve[-1] + 1, fsqrt(n) + 1)):
            if n % factor == 0:
                return False

    return True


def smallest_prime_factor(n: int, sieve: Sequence[int]=None) -> int:
    if n <= 1:
        raise ValueError(f'Cannot find smallest prime factor of {n}.')

    for factor in range(2, fsqrt(n) + 1) if sieve is None else sieve:
        if n % factor == 0:
            return factor

    return n


def generate_prime_factors(n: int, sieve: Sequence[int]=None) -> \
        Generator[int, None, None]:
    while n > 1:
        factor = smallest_prime_factor(n, sieve)

        yield factor

        while n % factor == 0:
            n //= factor


def generate_prime_factors_multiplicity(n: int, sieve: Sequence[int] = None) \
        -> Generator[Tuple[int, int], None, None]:
    while n > 1:
        factor = smallest_prime_factor(n, sieve)

        multiplicity = 0

        while n % factor == 0:
            n //= factor
            multiplicity += 1

        yield factor, multiplicity


def largest_prime_factor(n: int) -> int:
    if n <= 1:
        raise ValueError(f'Cannot find largest prime factor of {n}.')

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


def prime_sieve(n: int) -> Sequence[int]:
    """
    From here:

    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all
    -primes-below-n/3035188#3035188
    """
    import numpy as np

    if n <= 1:
        return [False] * n

    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool)

    for i in range(1, fsqrt(n) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False

    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0][1:] + 1) | 1)].tolist()


def primes_sequence() -> Generator[int, None, None]:
    for n in count(2):
        if is_prime(n):
            yield n

        n += 1
