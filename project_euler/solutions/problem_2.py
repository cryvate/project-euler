from ..library.sequences import fibonacci_sequence


def solve(bound: int=4_000_000) -> int:
    series = fibonacci_sequence()

    counter = 0

    for rabbits in series:
        if rabbits >= bound:
            break

        if rabbits % 2 == 0:
            counter += rabbits

    return counter
