from itertools import count

from typing import Generator

from .number_theory.primes import primes_sequence  # noqa: F401


def fibonacci_sequence() -> Generator[int, None, None]:
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


def collatz_sequence(n: int=13) -> Generator[int, None, None]:
    while n > 1:
        yield n

        if n % 2 == 0:
            n //= 2
        else:
            n *= 3
            n += 1

    yield 1


def triangle_sequence() -> Generator[int, None, None]:
    value = 0

    for n in count():
        yield value

        value += n + 1


def pentagonal_sequence() -> Generator[int, None, None]:
    value = 0

    for n in count():
        yield value

        value += 3 * n + 1


def hexagonal_sequence() -> Generator[int, None, None]:
    value = 0

    for n in count():
        yield value

        value += 4 * n + 1
