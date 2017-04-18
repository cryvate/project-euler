from itertools import count

from typing import Dict

from ..library.sqrt import is_square_fast


def shortest_integer(m: int, _cache: Dict[int, int]={}) -> int:
    if m in _cache:
        return _cache[m]

    if m == 0:
        _cache[m] = 0
        return 0

    counter = shortest_integer(m - 1)

    combineds = [i for i in range(1, 2 * m) if is_square_fast(i ** 2 + m ** 2)]

    for combined in combineds:
        if combined <= m:
            counter += combined // 2
        else:
            counter += m - ((combined - 1) // 2)

    _cache[m] = counter

    return counter


def solve(bound: int=1_000_000) -> int:
    for m in count():
        if shortest_integer(m) > bound:
            return m
