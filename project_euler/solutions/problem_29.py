from collections import Counter

from ..library.number_theory.primes import generate_prime_factors_multiplicity


def solve(bound: int=100) -> int:
    counters = []

    for n in range(2, bound + 1):
        counter = Counter()

        for prime, multiplicity in generate_prime_factors_multiplicity(n):
            counter[prime] = multiplicity

        counters.append(counter)

    terms = []

    for a in range(2, bound + 1):
        print(a)
        for b in range(2, bound + 1):
            result = Counter()

            for prime, multiplicity in counters[a - 2].items():
                result[prime] = multiplicity * b

            terms.append(tuple(result.items()))

    return len(set(terms))
