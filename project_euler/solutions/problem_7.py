from ..library.series import primes_nomemory_series as primes

def solve(number: int=10001) -> str:
    if number <= 0:
        raise ValueError

    for i, prime in enumerate(primes()):
        if i + 1 == number:
            return str(prime)