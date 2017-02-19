from project_euler.library.number_theory.primes import \
    prime_factor_trial_division_sqrt


def solve(n: int=600851475143) -> str:
    while True:
        factor = prime_factor_trial_division_sqrt(n)

        while n % factor == 0:
            n //= factor

        if n == 1:
            return str(factor)
