from itertools import count

from ..library.number_theory.primes import primes_sequence
from ..library.sqrt import is_square


def solve() -> int:
    primes = []
    primes_generator = primes_sequence()
    next(primes_generator)  # ignore 2 because even

    for n in count(3, 2):
        while not primes or primes[-1] <= n:
            primes.append(next(primes_generator))

        for prime in primes[:-1]:
            if is_square((n - prime) // 2):
                break
        else:
            return n
