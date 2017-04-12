from typing import List


def number_to_list(number: int, base: int = 10) -> List[int]:
    if number < 0:
        raise ValueError(f'Cannot convert {number} to list, must be positive.')
    if base <= 0:
        raise ValueError(f'Cannot convert to base {base}.')

    digits = []

    while number > 0:
        digits.append(number % base)

        number //= base

    return digits


def list_to_number(representation: List[int], base: int = 10) -> int:
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
