from math import factorial


def solve(n: int=100) -> str:
    return sum(int(digit) for digit in str(factorial(n)))
