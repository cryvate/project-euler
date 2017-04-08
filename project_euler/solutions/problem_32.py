from itertools import permutations


def solve() -> int:
    pandigital = []

    for permutation in permutations(range(1, 10)):
        result = int(''.join(str(digit) for digit in permutation[:4]))

        for i in range(1, 4):
            left = int(''.join(str(digit) for digit in permutation[4:4 + i]))
            right = int(''.join(str(digit) for digit in permutation[4 + i:]))

            if left * right == result:
                pandigital.append(result)

    return sum(set(pandigital))
