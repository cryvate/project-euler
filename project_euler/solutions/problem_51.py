from collections import Counter
from itertools import combinations

from ..library.number_theory.primes import is_prime, prime_sieve
from ..library.base import list_to_number, number_to_list


def solve() -> int:
    primes = prime_sieve(1_000_000)

    for prime in primes:
        if prime < 100_000:
            continue

        representation = number_to_list(prime)

        counter = Counter(representation)

        if max(counter.values()) < 3:
            continue

        masks = []

        for digit in counter:
            if digit > 2:  # because at least 8
                continue
            if counter[digit] >= 3:
                digit_at = [i for i, d in enumerate(representation)
                            if d == digit]
                masks += list(combinations(digit_at, 3))

        for mask in masks:
            masked_representation = list(representation)
            counter = 0

            for digit in range(10):
                for index in mask:
                    masked_representation[-index] = digit

                number = list_to_number(masked_representation)

                if is_prime(number, primes):
                    counter += 1

            if counter == 8:
                return prime
