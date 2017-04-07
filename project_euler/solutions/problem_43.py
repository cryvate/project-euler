from itertools import permutations, takewhile

from ..library.sequences import primes_sequence
from ..library.base import list_to_number


def solve() -> int:
    accumulate = 0

    primes = list(takewhile(lambda _, store=[True] * 7: store and store.pop(),
                            primes_sequence()))

    remaining = set(range(10))
    for d4 in range(0, 10, 2):
        remaining.remove(d4)
        for d5 in range(0, 10, 5):
            if d5 == d4:
                continue

            remaining.remove(d5)

            for permutation in permutations(remaining):
                number = permutation[:3] + (d4, ) + \
                         permutation[3:4] + (d5, ) + \
                         permutation[4:]

                for i in range(7):
                    if list_to_number(number[i + 1: i + 4]) % primes[i] != 0:
                        break
                else:
                    accumulate += list_to_number(number)

            remaining.add(d5)

        remaining.add(d4)

    return accumulate
