from itertools import permutations

from ..library.number_theory.primes import is_prime

from ..library.base import list_to_number


def solve() -> int:
    for n in range(9, -1, -1):
        if sum(range(n + 1)) % 3 == 0:
            continue  # always divisible by 3

        for permutation in permutations(range(n, 0, -1)):
            number = list_to_number(permutation)

            if is_prime(number):
                return number
