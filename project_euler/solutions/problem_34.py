from math import factorial


def solve() -> int:
    factorials = [factorial(digit) for digit in range(10)]

    bound = 0
    maximum = 0
    necessary = 0

    while maximum >= necessary:
        maximum += factorials[-1]
        necessary = 9 * necessary + 9

        bound += 1

    accumulate = 0

    for i in range(3, maximum + 1):
        if sum(factorials[int(digit)] for digit in str(i)) == i:
            print(i)
            accumulate += i

    return accumulate
