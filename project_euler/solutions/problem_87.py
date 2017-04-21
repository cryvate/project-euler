from collections import Counter

from ..library.number_theory.primes import prime_sieve
from ..library.sqrt import fsqrt


def solve(bound: int=50_000_000) -> int:
    max_power = 4
    primes = prime_sieve(fsqrt(bound))

    prime_powers = []

    for power in range(max_power, 1, -1):
        powers = []

        for prime in primes:
            prime_power = prime ** power

            if prime_power >= bound:
                break

            powers.append(prime_power)

        prime_powers.append(powers)

    counter = Counter()

    for fourth in prime_powers[0]:
        for third in prime_powers[1]:
            if fourth + third >= bound:
                break

            for second in prime_powers[2]:
                result = fourth + third + second

                if result >= bound:
                    break
                else:
                    counter[result] = 1

    return sum(counter.values())
