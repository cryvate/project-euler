from math import factorial


def solve(rows: int=20, columns: int=20) -> int:
    combs = factorial(rows + columns) // (factorial(rows) * factorial(columns))
    return combs
