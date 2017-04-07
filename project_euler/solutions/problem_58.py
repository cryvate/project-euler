from fractions import Fraction
from itertools import count

from ..library.number_theory.primes import is_prime


def solve(fraction: Fraction=Fraction(1, 10)) -> int:
    primes = 0
    for level in count(3, 2):
        print(level)
        primes += sum(
            is_prime(level ** 2 - (level - 1) * i) for i in range(1, 4))

        if primes < fraction * (2 * level - 1):
            return level
