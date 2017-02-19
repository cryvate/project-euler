from math import floor, gcd, sqrt


def solve(number: int=1000) -> str:
    if number <= 0 or number % 2 != 0:
        raise ValueError

    number //= 2

    for m in range(2, floor(sqrt(number)) + 1):
        if number % m == 0:
            remainder = number // m

            while remainder % 2 == 0:
                remainder //= 2

            if m % 2 == 0:
                k = m + 2
            else:
                k = m + 1

            for k in range(m + 1 + (m % 2), min(2 * m, remainder + 1), 2):
                if remainder % k == 0 and gcd(k, m) == 1:

                    d = number // (k * m)
                    n = k - m

                    a = d * (m * m - n * n)
                    b = 2 * m * n * d
                    c = d * (m * m + n * n)

                    return str(a * b * c)