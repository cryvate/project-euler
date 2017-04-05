from .primes import generate_prime_factors_multiplicity


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
