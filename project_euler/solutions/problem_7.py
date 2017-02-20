from ..library.sequences import primes_sequence as primes


def solve(number: int=10001) -> str:
    for i, prime in enumerate(primes()):
        if i + 1 == number:
            return str(prime)
