from math import factorial

from ..library.base import number_to_list, list_to_number, \
    count_permutations, range_combinations_digits


def solve(digits: int=6, terms=60, base: int=10) -> int:
    factorials = [factorial(n) for n in range(base)]

    def step(n: int) -> int:
        return sum(factorials[digit] for digit in number_to_list(n))

    counter = 0

    for combination in range_combinations_digits(1, digits + 1,
                                                 zero_included=False,
                                                 base=base):
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
                    counter += count_permutations(combination, True)

    return counter
