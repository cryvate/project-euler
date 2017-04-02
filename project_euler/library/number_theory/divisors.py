from .primes import generate_prime_factors_multiplicity


def divisor_count(n: int) -> int:
    no_divisors = 1

    for factor, multiplicity in generate_prime_factors_multiplicity(n):
        no_divisors *= (multiplicity + 1)

    return no_divisors
