def is_pandigital(n: int, zero_included: bool=False) -> bool:
    digits = str(n)
    return len(digits) == (10 if zero_included else 9) and \
        len(set(digits)) == (10 if zero_included else 9)
