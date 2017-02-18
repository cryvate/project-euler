from typing import Tuple

title = "Multiples of 3 and 5."

description = "If we list all the natural numbers below 10 that are" \
              " multiples" \
              " of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples" \
              " is 23." \
              "\n\n" \
              "Find the sum of all the multiples of 3 or 5 below 1000."

strategy = "Use a limited version of the Inclusion-Exclusion Principle."


def solve(bound: int=1000, divisors: Tuple[int, int]=(3, 5)) -> str:
    counter = 0

    for divisor in divisors:
        counter += sum(range(0, bound, divisor))

    counter -= sum(range(0, bound, divisors[0] * divisors[1]))

    return str(counter)
