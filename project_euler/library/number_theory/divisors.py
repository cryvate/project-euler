from typing import List

from .primes import generate_prime_factors_multiplicity


def divisors(n: int) -> List[int]:
    for factor, multiplicity in generate_prime_factors_multiplicity(n):
        result = []
        multiplier = 1
        remainder = n // (factor ** multiplicity)
        remainder_divisors = divisors(remainder)

        for exponent in range(multiplicity + 1):
            result += [multiplier * divisor for divisor in remainder_divisors]
            multiplier *= factor

        return result

    return [1]


def divisor_count(n: int) -> int:
    no_divisors = 1

    for factor, multiplicity in generate_prime_factors_multiplicity(n):
        no_divisors *= (multiplicity + 1)

    return no_divisors


def divisor_sum(n: int) -> int:
    sum_divisors = 1

    for factor, multiplicity in generate_prime_factors_multiplicity(n):
        sum_divisors *= (factor ** (multiplicity + 1) - 1) // (factor - 1)

    return sum_divisors


def divisor_range(n: int) -> List[int]:
    import numpy as np

    divisors = np.ones(n + 1, dtype=np.int64)
    divisors[0] = 0

    for i in range(2, n + 1):
        divisors[i::i] += i

    return divisors.tolist()
