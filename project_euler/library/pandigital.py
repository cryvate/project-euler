from .base import number_to_list


def is_pandigital(n: int, zero_included: bool=False) -> bool:
    digits = number_to_list(n)
    return len(digits) == (10 if zero_included else 9) and \
        set(digits) == (set(range(10)) if zero_included else set(range(1, 10)))
