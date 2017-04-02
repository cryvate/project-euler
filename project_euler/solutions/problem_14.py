from typing import Dict


def collatz_length(n: int, cache: Dict[int, int]={1: 1}) -> int:
    if n in cache:
        return cache[n]
    elif n % 2 == 0:
        cache[n] = collatz_length(n // 2) + 1
        return cache[n]
    else:
        cache[n] = collatz_length(3 * n + 1) + 1
        return cache[n]


def solve(bound: int=1_000_000) -> str:
    maximum_length = 0
    maximum_index = 0

    for n in range(1, bound):
        length = collatz_length(n)

        if length > maximum_length:
            maximum_length = length
            maximum_index = n

    return maximum_index
