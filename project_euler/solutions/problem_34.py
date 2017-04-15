from math import factorial

from ..library.base import number_to_list


def solve(base: int=10) -> int:
    factorials = [factorial(digit) for digit in range(base)]

    bound = 0
    maximum = 0
    necessary = 0

    while maximum >= necessary:
        maximum += factorials[-1]
        necessary = (base - 1) * necessary + (base - 1)

        bound += 1

    counter = 0

    for i in range(3, maximum + 1):
        if sum(factorials[digit] for digit in number_to_list(i)) == i:
            counter += i

    return counter
