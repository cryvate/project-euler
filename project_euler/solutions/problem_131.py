import itertools

from ..library.number_theory.primes import is_prime


def solve(bound: int=1_000_000) -> int:
    total = 0

    for n in itertools.count():
        difference = 3 * n * (n + 1) + 1

        if difference > bound:
            return total

        total += is_prime(difference)
