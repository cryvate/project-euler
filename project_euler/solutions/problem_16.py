def solve(base: int=2, exponent: int=1000) -> int:
    return str(sum(int(digit) for digit in str(base ** exponent)))
