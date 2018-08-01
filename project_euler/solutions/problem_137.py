from fractions import Fraction
import itertools

from ..library.sequences import fibonacci_sequence


def solve(bound: int=15) -> int:
    pair = list(itertools.islice(fibonacci_sequence(), 2 * bound + 2))[-2:]
    x = Fraction(*pair)
    return (x / (1 - x - x * x)).numerator
