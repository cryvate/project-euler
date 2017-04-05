from fractions import Fraction


def solve() -> int:
    multiplied = Fraction(1, 1)

    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if Fraction(i, k) == Fraction(i * 10 + j, j * 10 + k):
                    multiplied *= Fraction(i, k)

    return multiplied.denominator
