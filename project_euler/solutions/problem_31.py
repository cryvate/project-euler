from typing import List


def solve(n: int=200,
          allowable_partitions: List[int]=[1, 2, 5, 10, 20, 50, 100, 200]) \
        -> int:
    if n == 0:
        return 1

    if len(allowable_partitions) == 0:
        return 0

    accumulate = 0

    for i, amount in enumerate(allowable_partitions):
        for j in range(1, n // amount + 1):
            accumulate += solve(n - amount * j, allowable_partitions[:i])

    return accumulate
