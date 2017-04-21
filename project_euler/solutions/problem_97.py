def solve(digits: int=10) -> int:
    return (pow(2, 7830457, 10 ** digits) * 28433 + 1) % (10 ** digits)
