from collections import Counter
from itertools import count, combinations_with_replacement
from math import factorial

from typing import Generator, Iterable, List


def number_to_list(number: int, base: int=10) -> List[int]:
    if number < 0:
        raise ValueError(f'Cannot convert {number} to list, must be positive.')
    if base <= 0:
        raise ValueError(f'Cannot convert to base {base}.')

    digits = []

    while number > 0:
        digits.append(number % base)

        number //= base

    return list(reversed(digits))


def list_to_number(representation: Iterable[int], base: int = 10) -> int:
    accumulate = 0

    for digit in representation:
        accumulate = accumulate * base + digit

    return accumulate


def is_permutation(self: int, other: int, base: int = 10) -> bool:
    if self // other >= base or other // self >= base:
        return False
    else:
        return sorted(number_to_list(self, base)) == \
            sorted(number_to_list(other, base))


def range_combinations_digits(start: int=0,
                              *args,
                              zero_included: bool=True,
                              base: int=10) -> Generator[int, None, None]:
    iterator = range(start, *args)

    for length in iterator:
        local_iterator = combinations_with_replacement(range(not zero_included,
                                                             base),
                                                       length)

        if length != 0:
            next(local_iterator)

        yield from local_iterator


def count_combinations_digits(start: int=0,
                              step: int=None,
                              zero_included: bool=True,
                              base: int=10) -> Generator[int, None, None]:
    iterator = count(start, step) if step else count(start)

    for length in iterator:
        local_iterator = combinations_with_replacement(range(not zero_included,
                                                             base),
                                                       length)

        if length != 0:
            next(local_iterator)

        yield from local_iterator


def count_permutations(digits: List[int],
                       one_also_zero_not_leading: bool=False) -> int:
    length = len(digits)

    contribution = factorial(length)

    digit_counter = Counter(digits)

    for value in digit_counter.values():
        contribution //= factorial(value)

    if one_also_zero_not_leading and 1 in digit_counter:
        ones = digit_counter[1]
        contribution += (contribution // length) * \
                        (length - ones)

    return contribution
