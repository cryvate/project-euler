from typing import List, Iterable

from ..sequences import pentagonal_sequence, negative_pentagonal_sequence


def partitions(n, cache: List=[1], length: List[int]=[1]) -> int:
    # needs to be called in order, starting at 1

    if n < length[0]:
        return cache[n]

    if n > length[0]:
        for k in range(length[0], n):
            partitions(k)

        return partitions(n)

    accumulate = 0

    sign = -1

    for pos, neg in zip(pentagonal_sequence(), negative_pentagonal_sequence()):
        if pos == 0:
            continue

        sign *= -1

        if n - pos < 0:
            break

        accumulate += sign * cache[n - pos]

        if n - neg < 0:
            continue

        accumulate += sign * cache[n - neg]

    cache.append(accumulate)
    length[0] += 1

    return accumulate


class Partitions:
    def __init__(self, numbers: Iterable[int]=None) -> None:
        self.numbers = list(numbers)
        self._cache = {}

    def __getitem__(self, item: int) -> int:
        return self(item)

    def __call__(self, n: int, max_index: int=None) -> int:
        numbers = self.numbers

        if max_index is None:
            max_index = len(numbers)

        arguments = (n, max_index)

        if arguments in self._cache:
            return self._cache[arguments]

        accumulate = 0

        if n == 0:
            accumulate = 1
        elif max_index == 0:
            pass
        else:
            for i, value in enumerate(numbers[:max_index]):
                for k in range(1, n // value + 1):
                    accumulate += self(n - value * k, i)

        self._cache[arguments] = accumulate

        return self._cache[arguments]
