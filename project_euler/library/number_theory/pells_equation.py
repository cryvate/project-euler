from .continued_fractions import convergents_sqrt

from typing import Generator, Tuple


def solve_pells_equation(n: int) -> Generator[Tuple[int, int], None, None]:
    convergents = convergents_sqrt(n)

    for convergent in convergents:
        h = convergent.numerator
        k = convergent.denominator

        if h ** 2 - n * (k ** 2) == 1:
            break

    x, y = h, k

    while True:
        yield x, y
        x, y = h * x + n * k * y, h * y + k * x


def solve_negative_pells_equation(n: int) -> \
        Generator[Tuple[int, int], None, None]:
    convergents = convergents_sqrt(n)

    for convergent in convergents:
        h = convergent.numerator
        k = convergent.denominator

        if h ** 2 - n * (k ** 2) == -1:
            break

        if h ** 2 - n * (k ** 2) == 1:
            raise ValueError(f"Equation x^2 - {n}y^2 = -1 has no solution")

    x, y = h, k

    while True:
        yield x, y
        x, y = h * x + n * k * y, h * y + k * x
        x, y = h * x + n * k * y, h * y + k * x
