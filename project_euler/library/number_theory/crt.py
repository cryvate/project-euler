from .bezout import bezout
from .gcd import gcd


def crt(a: int, m: int, b: int, n: int) -> int:
    common = gcd(m, n)

    quotient, remainder = divmod(b - a, common)

    if remainder != 0:
        raise ValueError(f'Trying to solve system that is inconsistent, '
                         f'gcd = {common} but a - b = {a - b}.')

    inverse = bezout(m // common, n // common)[0]

    return (m * inverse * quotient + a) % ((m * n) // common)
