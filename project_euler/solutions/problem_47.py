from itertools import count

from ..library.number_theory.primes import generate_prime_factors


def solve(factors: int=4, consecutive: int=4) -> int:
    run = 0

    for n in count():
        if n == 0:
            continue

        if n == 1:
            continue

        for i, factor in enumerate(generate_prime_factors(n)):
            if i >= factors:
                run = 0
                break
        else:
            if i == factors - 1:
                run += 1
            else:
                run = 0

        if run == consecutive:
            return n - run + 1
