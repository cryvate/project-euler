from math import factorial

from ..library.base import count_combinations_digits, list_to_number, \
    number_to_list


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

    for combination in count_combinations_digits(2,  # ignore single numbers
                                                 base=base,
                                                 zero_included=True):
        if list_to_number(sorted(combination)) >= maximum * 10:
            return counter

        attempt = sum(factorials[digit] for digit in combination)

        if sorted(number_to_list(attempt)) == list(combination):
            counter += attempt
