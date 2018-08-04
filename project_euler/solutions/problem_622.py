from ..library.number_theory.primes import generate_prime_factors
from ..library.number_theory.divisors import divisors


def solve(bound: int=60):
    total = 0
    prime_factors = list(generate_prime_factors(bound))

    for divisor in sorted(divisors(2 ** bound - 1)):
        for prime in prime_factors:
            if (2 ** (bound // prime) - 1) % divisor == 0:
                break
        else:
            total += divisor + 1

    return total
