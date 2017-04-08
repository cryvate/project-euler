from itertools import count

from typing import Generator, Sequence, Tuple

from ..sqrt import fsqrt


def is_prime(n: int, sieve: Sequence[int]=None) -> bool:
    if n <= 1:
        return False

    for factor in range(2, fsqrt(n) + 1) if sieve is None else sieve:
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


def primes_sequence() -> Generator[int, None, None]:
    for n in count(2):
        if is_prime(n):
            yield n

        n += 1
