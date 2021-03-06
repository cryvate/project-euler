from typing import List, Iterable

Partition = List[int]


def partitions(n: int, cache: List=[1], length: List[int]=[1]) -> int:
    if n < length[0]:
        return cache[n]

    if n > length[0]:
        for k in range(length[0], n):
            partitions(k)

        return partitions(n)

    accumulate = 0

    sign = -1

    # could use (negative) pentagonal sequence, but is slower.
    for i in range(2 * n):
        pos = (i * (3 * i - 1)) // 2
        neg = (i * (3 * i + 1)) // 2

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
        if numbers is None:
            self.numbers = None
        else:
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


class GeneratePartitions(Partitions):
    def __call__(self, n: int, max_index: int=None) -> List[Partitions]:
        numbers = self.numbers

        if numbers is None:
            numbers = [i for i in range(1, n + 1)]

        if max_index is None:
            max_index = len(numbers)

        arguments = (n, max_index)

        if arguments in self._cache:
            return self._cache[arguments]

        accumulate = []

        if n == 0:
            accumulate.append([])
        elif max_index == 0:
            pass
        else:
            for i, value in enumerate(numbers[:max_index]):
                for k in range(1, n // value + 1):
                    minor = self(n - value * k, i)

                    for partition in minor:
                        accumulate.append([value] * k + partition)

        self._cache[arguments] = accumulate

        return self._cache[arguments]
