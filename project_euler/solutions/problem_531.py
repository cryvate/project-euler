from typing import Iterable
from ..library.number_theory.euler_totient import phi
from ..library.number_theory.crt import crt


def solve(number_range: Iterable[int]=list(range(1_000_000, 1_005_000))) -> \
        str:
    numbers = sorted([n for n in number_range])
    phis = [phi(n) for n in numbers]

    total = 0

    for m, a in zip(numbers, phis):
        for n, b in zip(numbers, phis):
            if n >= m:
                break

            try:
                answer = crt(a, m, b, n)
                total += answer
            except ValueError:
                pass

    return str(total)
