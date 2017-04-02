from itertools import count


def fibonacci_sequence() -> int:
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


def primes_sequence() -> int:
    from project_euler.library.number_theory.primes import is_prime

    for n in count(2):
        if is_prime(n):
            yield n

        n += 1


def collatz_sequence(n: int=13) -> int:
    while n > 1:
        yield n

        if n % 2 == 0:
            n //= 2
        else:
            n *= 3
            n += 1

    yield 1
