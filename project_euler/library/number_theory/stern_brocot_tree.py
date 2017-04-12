from fractions import Fraction
from queue import Queue

from typing import Callable, Generator


def mediant(left: Fraction, right: Fraction) -> Fraction:
    return Fraction(left.numerator + right.numerator,
                    left.denominator + right.denominator)


def stern_brocot_tree(left: Fraction=Fraction(0, 1),
                      right: Fraction=Fraction(1, 1),
                      classifier: Callable[[Fraction], bool] = None) \
        -> Generator[Fraction, None, None]:
    queue = Queue()

    queue.put((left, right))

    while not queue.empty():
        left, right = queue.get()

        median = mediant(left, right)

        if classifier is None or classifier(median):
            yield median

            queue.put((left, median))
            queue.put((median, right))
