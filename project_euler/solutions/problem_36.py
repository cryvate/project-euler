from ..library.palindrome import is_palindrome


def solve(bound: int=1_000_000) -> int:
    return sum(n for n in range(1, bound + 1) if
               is_palindrome(n, 10) and is_palindrome(n, 2))
