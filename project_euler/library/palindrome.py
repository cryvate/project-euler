from .base import number_to_list


def is_palindrome(n: int, base: int=10) -> bool:
    if n == 0:
        return False

    representation = number_to_list(n, base)

    for digit, reverse_digit in zip(representation, reversed(representation)):
        if digit != reverse_digit:
            return False

    return True
