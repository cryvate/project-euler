from math import gcd

from ..library.sqrt import fsqrt


def solve(number: int=1000) -> int:
    if number <= 0 or number % 2 != 0:
        raise ValueError

    number //= 2

    for m in range(2, fsqrt(number) + 1):
        if number % m == 0:
            remainder = number // m

            while remainder % 2 == 0:
                remainder //= 2

            for k in range(m + 1 + (m % 2), min(2 * m, remainder + 1), 2):
                if remainder % k == 0 and gcd(k, m) == 1:

                    d = number // (k * m)
                    n = k - m

                    a = d * (m * m - n * n)
                    b = 2 * m * n * d
                    c = d * (m * m + n * n)

                    return a * b * c
