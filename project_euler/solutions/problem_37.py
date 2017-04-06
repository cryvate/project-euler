from itertools import count

from ..library.number_theory.primes import is_prime


def is_truncatable_prime(n: int) -> bool:
    str_n = str(n)
    for digit in str_n:
        if int(digit) % 2 == 0 and int(digit) != 2:
            return False

    if not is_prime(n):
        return False

    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i])):
            return False

    return True


def solve() -> int:
    total = 11
    found = 0
    accumulate = 0

    for n in count():
        if n < 9:  # I disagree with of not including them vehemently
            continue

        if is_truncatable_prime(n):
            accumulate += n
            found += 1

            if found >= total:
                return accumulate
