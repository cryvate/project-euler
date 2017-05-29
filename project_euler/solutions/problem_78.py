from itertools import count

from ..library.combinatorics.partitions import partitions


def solve(divisor: int=1_000_000) -> int:
    for n in count(1):
        if partitions(n) % divisor == 0:
            return n
