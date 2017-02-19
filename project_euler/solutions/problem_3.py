from project_euler.library.number_theory.primes import smallest_prime_factor


def solve(n: int=600851475143) -> str:
    while True:
        factor = smallest_prime_factor(n)

        while n % factor == 0:
            n //= factor

        if n == 1:
            return str(factor)
