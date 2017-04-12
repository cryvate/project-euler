from ..library.number_theory.primes import primes_sequence


def solve(bound: int=1_000_000):
    accumulate = 1
    relative = 1

    primes = primes_sequence()

    for prime in primes:
        if accumulate * prime > bound:
            return accumulate
        else:
            accumulate *= prime
            relative *= prime - 1
