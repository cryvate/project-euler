from itertools import count


def fibonacci_series():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


def primes_series():
    from project_euler.library.number_theory.primes import is_prime_trial_division_sqrt \
                                             as is_prime

    for n in count(2):
        if is_prime(n):
            yield n

        n += 1
