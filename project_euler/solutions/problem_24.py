from itertools import count
from math import factorial
from typing import List


def lexicographic_index(to_permute: List[int], index: int) -> List[int]:
    if index == 0:
        return to_permute

    length = len(to_permute)

    if index >= factorial(length):
        raise ValueError(f'Cannot find permutation at index {index} since '
                         f'list to permute {to_permute} only has length '
                         f'{length} and so can index to below '
                         f'{factorial(length)}. Note index starts at 0.')

    for i in count():
        if factorial(i) > index:
            left, right = divmod(index, factorial(i - 1))

            to_permute[-i], to_permute[-i + left] = \
                to_permute[-i + left], to_permute[-i]

            left_result = to_permute[:-i + 1]
            right_result = lexicographic_index(sorted(to_permute[-i + 1:]),
                                               right)

            return left_result + right_result


def solve(n: int=1_000_000) -> str:
    return ''.join(str(i) for i in lexicographic_index(list(range(10)), n - 1))
