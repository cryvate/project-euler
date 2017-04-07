from ..library.number_theory.primes import is_prime, prime_sieve


def solve(bound: int=1_000_000, minimal_length=21) -> int:
    upto = (bound + 1) // minimal_length
    primes = prime_sieve(upto)

    for length in range(len(primes), 0, -1):
        for i in range(0, len(primes) - length):
            consecutive_sum = sum(primes[i:i + length])
            if consecutive_sum > bound:
                break
            if is_prime(consecutive_sum, sieve=primes):
                return consecutive_sum
