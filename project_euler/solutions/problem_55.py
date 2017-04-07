from ..library.palindrome import is_palindrome
from ..library.base import list_to_number, number_to_list


def is_lychrel(n: int) -> bool:
    for i in range(51):
        n += list_to_number(number_to_list(n))

        if is_palindrome(n):
            return False

    return True


def solve() -> int:
    """could parametrize, but Lychrel results not given outside bound"""

    return sum(1 for n in range(1, 10_000) if is_lychrel(n))
