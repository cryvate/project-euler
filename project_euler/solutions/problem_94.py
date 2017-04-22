from collections import deque

from ..library.number_theory.pythagorean_triples import PythagoreanTriplet


def solve(bound: int=1_000_000_000) -> int:
    accumulate = 0

    def process(triplet: PythagoreanTriplet) -> bool:
        nonlocal accumulate

        minimal = triplet[0] if triplet[0] <= triplet[1] else triplet[1]
        perimeter = minimal * 2 + 2 * triplet[2]

        if perimeter > bound:
            return False

        difference = minimal * 2 - triplet[2]

        if difference == 1 or difference == -1:
            accumulate += perimeter

        return True

    queue = deque()

    start = (3, 4, 5)
    process(start)

    queue.append((3, 4, 5))

    while queue:
        a, b, c = queue.popleft()

        new = (
            a - 2 * b + 2 * c,
            2 * a - b + 2 * c,
            2 * a - 2 * b + 3 * c
        )

        if process(new):
            queue.append(new)

        new = (
            -a + 2 * b + 2 * c,
            -2 * a + b + 2 * c,
            -2 * a + 2 * b + 3 * c
        )

        if process(new):
            queue.append(new)

    return accumulate
