from typing import Iterable

from project_euler.library.sequences import pentagonal_sequence, negative_pentagonal_sequence


def partitions(n, numbers: Iterable[int]=None) -> int:
    partitions_class = Partitions(numbers)

    return partitions_class(n)


class Partitions:
    def __init__(self, numbers: Iterable[int]=None) -> None:
        self.numbers = list(numbers) if numbers is not None else None
        self._cache = {}

    def __call__(self, n: int, max_index: int=None) -> int:
        if self.numbers is None:
            numbers = range(1, n + 1)
        else:
            numbers = self.numbers

        if max_index is None:
            max_index = len(numbers)

        arguments = (n, max_index)

        if arguments in self._cache:
            return self._cache[arguments]

        accumulate = 0

        if n == 0:
            accumulate = 1
        if self.numbers is None:
            sign = -1

            for pos, neg in zip(pentagonal_sequence(),
                                negative_pentagonal_sequence()):
                if pos == 0:
                    continue

                sign *= -1

                if n - pos < 0:
                    break

                accumulate += sign * self(n - pos)

                if n - neg < 0:
                    break

                accumulate += sign * self(n - neg)
        elif max_index == 0:
            pass
        else:
            for i, value in enumerate(numbers[:max_index]):
                for k in range(1, n // value + 1):
                    accumulate += self(n - value * k, i)

        self._cache[arguments] = accumulate

        return self._cache[arguments]
