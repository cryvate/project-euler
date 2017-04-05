from ..library.number_theory.divisors import divisor_sum


def abundant(n: int) -> bool:
    return divisor_sum(n) > 2 * n


def solve(bound: int=28_123) -> int:
    abundants = [n for n in range(1, bound + 1) if abundant(n)]

    covered = [False for n in range(bound + 1)]

    for i, n in enumerate(abundants):
        for m in abundants[i:]:
            if n + m > bound:
                continue

            covered[n + m] = True

    return sum(n for n in range(bound + 1) if not covered[n])
