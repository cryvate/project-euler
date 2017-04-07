from ..library.sequences import pentagonal_sequence
from ..library.sqrt import fsqrt, is_square_fast


def is_pentagonal(n: int) -> bool:
    if not is_square_fast(24 * n + 1):
        return False

    return (fsqrt(24 * n + 1) + 1) % 6 == 0


def solve() -> int:
    pentagonals = []
    found = False
    minimal = -1

    for higher in pentagonal_sequence():
        if higher == 0:
            continue

        if found and higher - pentagonals[-1] >= found:
            return minimal

        for i, lower in enumerate(reversed(pentagonals)):
            if found and higher - lower >= found:
                pentagonals = pentagonals[-i:]
                break
            if is_pentagonal(higher - lower) and is_pentagonal(higher + lower):
                minimal = higher - lower
                found = True

        pentagonals.append(higher)
