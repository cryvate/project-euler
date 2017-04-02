from math import factorial


def solve(n: int=100) -> str:
    return str(sum(int(digit) for digit in str(factorial(n))))
