from ..library.sequences import primes_sequence as primes


def solve(number: int=10001) -> int:
    for i, prime in enumerate(primes()):
        if i + 1 == number:
            return prime
