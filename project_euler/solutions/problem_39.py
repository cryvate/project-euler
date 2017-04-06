from ..library.number_theory.pythagorean_triples import \
    primitive_pythagorean_triples


def solve(perimeter_bound: int=1_000) -> int:
    solutions = [0 for _ in range(perimeter_bound + 1)]

    triplets = primitive_pythagorean_triples(
        valid=lambda triplet: sum(triplet) <= perimeter_bound
    )

    for triplet in triplets:
        for multiplier in range(1, perimeter_bound // sum(triplet) + 1):
            solutions[sum(triplet) * multiplier] += 1

    return solutions.index(max(solutions))
