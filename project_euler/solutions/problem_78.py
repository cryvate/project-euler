from itertools import count

from ..library.combinatorics.partitions import Partitions


def solve(divisor: int=1_000_000) -> int:
    partitions = Partitions()

    for n in count(2):
        if partitions(n) % divisor == 0:
            return n
