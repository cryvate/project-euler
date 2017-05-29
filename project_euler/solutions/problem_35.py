from typing import List

from ..library.base import number_to_list, list_to_number
from ..library.sqrt import fsqrt
from ..library.number_theory.primes import is_prime, prime_sieve


def is_circular_prime(n: int, sieve: List[int]) -> bool:
    rep_n = number_to_list(n)

    for digit in rep_n:
        if digit % 2 == 0:
            return False

    for i in range(len(rep_n)):
        if not is_prime(list_to_number(rep_n[i:] + rep_n[:i]), sieve):
            return False

    return True


def solve(digits: int=6) -> int:
    bound = 10 ** digits
    sieve = prime_sieve(fsqrt(bound))

    return sum(1 for prime in range(1, bound)
               if is_circular_prime(prime, sieve)) + 1  # 2
