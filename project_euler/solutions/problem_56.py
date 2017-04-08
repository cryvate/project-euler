from ..library.base import number_to_list


def solve(bound: int=100):
    maximal = 0

    for a in range(bound):
        for b in range(bound):
            sum_digits = sum(number_to_list(a ** b))

            if sum_digits > maximal:
                maximal = sum_digits

    return maximal
