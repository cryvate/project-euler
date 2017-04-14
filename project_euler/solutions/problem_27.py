from itertools import count

from ..library.number_theory.primes import is_prime


def consecutive(a: int, b: int, sieve) -> int:
    for n in count():
        if not is_prime(n ** 2 + a * n + b, sieve):
            return n


def solve(a_bound: int=1_000, b_bound: int=1_000, sieve_bound: int=100) -> int:
    maximum = 0
    a_max = 0
    b_max = 0

    sieve = [n for n in range(sieve_bound) if is_prime(n)]

    for a in range(-a_bound, a_bound + 1):
        for b in range(-b_bound, b_bound + 1):
            present = consecutive(a, b, sieve)

            if present > maximum:
                maximum = present
                a_max = a
                b_max = b

    return a_max * b_max
