from fractions import Fraction
from queue import Queue

from typing import Callable, Generator

from .euler_totient import phi_range


def mediant(left: Fraction, right: Fraction) -> Fraction:
    return Fraction(left.numerator + right.numerator,
                    left.denominator + right.denominator)


def stern_brocot_tree(left: Fraction=Fraction(0, 1),
                      right: Fraction=Fraction(1, 1),
                      classifier: Callable[[Fraction], bool]=None,
                      depth: int=None) -> \
        Generator[Fraction, None, None]:
    queue = Queue()

    queue.put((left, right))

    while not queue.empty():
        left, right = queue.get()

        median = mediant(left, right)

        if classifier is not None and not classifier(median):
            continue
        if depth is not None and median.denominator > depth:
            continue

        yield median

        queue.put((left, median))
        queue.put((median, right))


def size_stern_brocot_tree(depth: int=None) -> int:
    return sum(phi_range(depth)) - 1
