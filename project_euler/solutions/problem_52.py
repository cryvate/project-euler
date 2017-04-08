from collections import Counter
from itertools import count

from ..library.base import number_to_list


def solve(max_multiplier: int=6) -> int:
    for n in count():
        if n == 0:
            continue

        counter = Counter(number_to_list(n))

        for multiplier in range(2, max_multiplier + 1):
            if counter != Counter(number_to_list(n * multiplier)):
                break
        else:
            return n
