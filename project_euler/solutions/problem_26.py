from ..library.fraction_representation import unit_fraction_to_representation


def solve(bound: int=1_000) -> int:
    max_found = 0
    index = 0

    denominator = bound - 1

    for denominator in range(bound - 1, 1, -1):
        if denominator <= max_found:
            break

        length = unit_fraction_to_representation(denominator)[1][1]

        if length > max_found:
            max_found = max(max_found, length)
            index = denominator

    return index
