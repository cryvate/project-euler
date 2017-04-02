from math import factorial


def solve(rows: int=20, columns: int=20) -> str:
    combs = factorial(rows + columns) // (factorial(rows) * factorial(columns))
    return str(combs)
