from collections import Counter
from itertools import combinations_with_replacement
from math import factorial

from ..library.base import number_to_list, list_to_number


def solve(digits: int=6, terms=60, base: int=10) -> int:
    factorials = [factorial(n) for n in range(base)]

    def step(n: int) -> int:
        return sum(factorials[digit] for digit in number_to_list(n))

    counter = 0

    for level in range(1, digits + 1):
        for combination in combinations_with_replacement(range(1, 10), level):
            concatenated = list_to_number(combination)

            n = concatenated
            visited = []
            steps = 0

            while n not in visited:
                visited.append(n)
                n = step(n)
                steps += 1

                if steps > terms:
                    break
            else:
                if steps == terms:
                    contribution = factorial(level)

                    digit_counter = Counter(combination)

                    for value in digit_counter.values():
                        contribution //= factorial(value)

                    if 1 in digit_counter:
                        ones = digit_counter[1]
                        contribution += (contribution // level) * \
                                        (level - ones)

                    counter += contribution

    return counter
