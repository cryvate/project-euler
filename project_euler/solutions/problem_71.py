from fractions import Fraction


def mediant(self: Fraction, other: Fraction) -> Fraction:
    return Fraction(self.numerator + other.numerator,
                    self.denominator + other.denominator)


def solve(bound: int=1_000_000) -> int:
    old_median = Fraction(0)
    median = Fraction(0)
    right = Fraction(3, 7)

    while median.denominator <= bound:
        old_median, median = median, mediant(median, right)

    return old_median.numerator
