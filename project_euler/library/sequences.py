from itertools import count


def fibonacci_sequence():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


def primes_sequence():
    from project_euler.library.number_theory.primes import is_prime

    for n in count(2):
        if is_prime(n):
            yield n

        n += 1
