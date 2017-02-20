from .primes import generate_prime_factors


def phi(n: int) -> int:
    result = n

    for factor in generate_prime_factors(n):
        result *= (factor - 1)
        result //= factor

    return result
