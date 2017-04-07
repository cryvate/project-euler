from collections import Counter

from ..library.number_theory.primes import is_prime
from ..library.base import number_to_list


def solve() -> str:
    primes = [(tuple(sorted(number_to_list(n))), n)
              for n in range(1_000, 10_000) if is_prime(n)]

    counter = Counter(sorted_representation for sorted_representation, _
                      in primes)
    representations = []

    for sorted_representation, repeats in counter.items():
        if repeats >= 3:
            representations.append(sorted_representation)

    per_representation = {representation: [] for representation
                          in representations}

    for sorted_representation, p in primes:
        if sorted_representation in representations:
            per_representation[sorted_representation].append(p)

    for representation in representations:
        sorted_primes = sorted(per_representation[representation])

        for i, p in enumerate(sorted_primes):
            for q in sorted_primes[i + 2:]:
                if p == 1487:  # ignored
                    continue

                if (p - q) % 2 == 0 and (p + q) // 2 in sorted_primes:
                    return str(p) + str((p + q) // 2) + str(q)
