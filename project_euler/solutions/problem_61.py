from collections import Counter

from typing import Optional, Tuple

from ..library.sequences import triangle_sequence, \
                                square_sequence, \
                                pentagonal_sequence, \
                                hexagonal_sequence, \
                                heptagonal_sequence, \
                                octagonal_sequence, \
                                find_intersection_interval


def solve() -> int:
    sequences = [triangle_sequence(), square_sequence(),
                 pentagonal_sequence(), hexagonal_sequence(),
                 heptagonal_sequence(), octagonal_sequence()]
    allowable = [list(find_intersection_interval(sequence, 10 ** 3, 10 ** 4))
                 for sequence in sequences]

    vertices = []

    for i, allowables in enumerate(allowable):
        for number in allowables:
            vertices.append((i, number))

    edges = {}

    for i, source in vertices:
        edges[(i, source)] = []
        for j, target in vertices:
            if i == j:
                continue

            if str(source)[2:] != str(target)[:2]:
                continue

            edges[(i, source)] += [(j, target)]

    remaining = Counter(range(len(allowable)))

    def iterate(current: Tuple[int, int]=None,
                first: int=None) -> Optional[int]:
        for j, target in vertices if (current is None) else edges[current]:
            if remaining[j] == 0:
                continue

            if first is None:
                remaining[j] = 0
                result = iterate((j, target), (j, target))
                remaining[j] = 1
            elif sum(remaining.values()) == 1:
                if first in edges[(j, target)]:
                    return target
                else:
                    return None
            else:
                remaining[j] = 0
                result = iterate((j, target), first)
                remaining[j] = 1

            if result is not None:
                print(target)
                return result + target

        return None

    return iterate()
