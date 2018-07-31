from itertools import count

from typing import Callable, Generator, Iterable, List

from .number_theory.primes import primes_sequence  # noqa: F401


def fibonacci_sequence() -> Iterable[int]:
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


def collatz_sequence(n: int=13) -> Iterable[int]:
    while n > 1:
        yield n

        if n % 2 == 0:
            n //= 2
        else:
            n *= 3
            n += 1

    yield 1


def create_polynomial_sequence(coefficients: List[int]) -> \
        Callable[[], Iterable[int]]:
    # do not create copy of list: can change on the fly to provide flexibility
    def polynomial_sequence(start: int=0) -> Iterable[int]:
        value = 0

        for n in count():
            if n >= start:
                yield value

            power = 1

            for coefficient in coefficients:
                value += coefficient * power
                power *= n

    return polynomial_sequence


triangle_sequence = create_polynomial_sequence([1, 1])
square_sequence = create_polynomial_sequence([1, 2])
pentagonal_sequence = create_polynomial_sequence([1, 3])
negative_pentagonal_sequence = create_polynomial_sequence([2, 3])

hexagonal_sequence = create_polynomial_sequence([1, 4])
heptagonal_sequence = create_polynomial_sequence([1, 5])
octagonal_sequence = create_polynomial_sequence([1, 6])
cube_sequence = create_polynomial_sequence([1, 3, 3])


def find_intersection_interval(sequence: Iterable[int],
                               begin: int=None,
                               end: int=None,
                               breaking: bool=True) -> \
        Iterable[int]:
    for value in sequence:
        if end is not None and value >= end:
            if breaking:
                break
            else:
                continue  # pragma: no cover
                # peephole optimizer says not covered, but it is

        if begin is not None and value >= begin:
            yield value
