from typing import List, Tuple


def product_sum_count(bound: float,
                      minimal: int=2) -> List[Tuple[int, int, int]]:
    for i in range(minimal, int(bound) + 1):
        current = (i, i, 1)
        yield current

        for p, s, c in product_sum_count(bound / i, minimal):

            yield (p * i, s + i, c + 1)


def solve(bound: int=12_000) -> int:
    minimal_for_k = [0 for k in range(bound + 1)]

    for p, s, c in product_sum_count(2 * bound):
        k = p - s + c

        if k <= 1 or k > bound:
            continue

        current = minimal_for_k[k]

        if current == 0 or p < current:
            minimal_for_k[k] = p

    return sum(set(minimal_for_k))
