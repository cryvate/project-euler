from itertools import combinations_with_replacement

from ..library.base import number_to_list, count_permutations


def solve(digits: int=7):
    squares = [i ** 2 for i in range(10)]
    maximum = digits * 9 ** 2

    goes_to_89 = [False for _ in range(maximum + 1)]

    for n in range(1, maximum + 1):
        m = n
        while m != 1 and m != 89:
            m = sum(squares[digit] for digit in number_to_list(m))

        goes_to_89[n] = (m == 89)

    accumulate = 0

    for combination in combinations_with_replacement(range(10), digits):
        if goes_to_89[sum(squares[digit] for digit in combination)]:
            accumulate += count_permutations(combination)

    return accumulate
