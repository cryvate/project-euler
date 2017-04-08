from collections import deque

from typing import Callable, Tuple

PythagoreanTriplet = Tuple[int, int, int]


def primitive_pythagorean_triples(valid:
                                  Callable[[PythagoreanTriplet], bool]=None,
                                  starting: PythagoreanTriplet=(3, 4, 5)) -> \
        PythagoreanTriplet:
    queue = deque()

    queue.append(starting)

    while queue:
        a, b, c = queue.popleft()

        if valid and not valid((a, b, c)):
            continue

        yield a, b, c

        queue.append((
            a - 2 * b + 2 * c,
            2 * a - b + 2 * c,
            2 * a - 2 * b + 3 * c
        ))

        queue.append((
            a + 2 * b + 2 * c,
            2 * a + b + 2 * c,
            2 * a + 2 * b + 3 * c
        ))

        queue.append((
            -a + 2 * b + 2 * c,
            -2 * a + b + 2 * c,
            -2 * a + 2 * b + 3 * c
        ))
