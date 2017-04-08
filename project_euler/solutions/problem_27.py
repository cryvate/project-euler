from itertools import count

from ..library.number_theory.primes import is_prime


def consecutive(a: int, b: int) -> int:
    for n in count():
        if not is_prime(n ** 2 + a * n + b):
            return n


def solve(a_bound: int=1_000, b_bound: int=1_000) -> int:
    maximum = 0
    a_max = 0
    b_max = 0

    for a in range(-a_bound, a_bound + 1):
        for b in range(-b_bound, b_bound + 1):
            present = consecutive(a, b)

            if present > maximum:
                maximum = present
                a_max = a
                b_max = b

    return a_max * b_max
