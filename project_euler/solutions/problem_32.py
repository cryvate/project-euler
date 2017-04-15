from itertools import permutations

from ..library.base import list_to_number


def solve() -> int:
    pandigital = []

    for permutation in permutations(range(1, 10)):
        result = list_to_number(permutation[:4])

        for i in range(1, 4):
            left = list_to_number(permutation[4:4 + i])
            right = list_to_number(permutation[4 + i:])

            if left * right == result:
                pandigital.append(result)

    return sum(set(pandigital))
