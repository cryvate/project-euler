from .base import number_to_list


def is_pandigital(number: int, zero_included: bool=False) -> bool:
    if not zero_included:
        return is_pandigital_n(number, 9)

    digits = number_to_list(number)

    return len(digits) == 10 and set(digits) == set(range(10))


def is_pandigital_n(number: int, n: int) -> bool:
    digits = number_to_list(number)
    return len(digits) == n and set(digits) == set(range(1, n + 1))
