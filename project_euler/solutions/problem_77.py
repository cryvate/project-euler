from itertools import count

from ..library.combinatorics.partitions import Partitions
from ..library.number_theory.primes import is_prime


def solve(bound: int=5_000) -> int:
    primes = []
    partitions_class = Partitions(primes)
    # use explicit partition class, because we want to dynamically add to
    # numbers to consider for partition, but want to keep old results, as they
    # are still valid.

    for n in count(2):
        if is_prime(n):
            partitions_class.numbers.append(n)

        if partitions_class(n) > bound:
            return n
