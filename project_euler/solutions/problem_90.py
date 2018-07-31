from itertools import combinations


REQUIRED = [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5), (3, 6), (4, 6), (4, 6),
            (1, 8)]


def solve() -> int:
    accumulate = 0

    digits = list(range(9)) + [6]

    for first_die in combinations(digits, 6):
        for second_die in combinations(digits, 6):
            if second_die > first_die:
                break

            for i, j in REQUIRED:  # works because i != j in all cases
                for k in first_die:
                    if k == i:
                        for m in second_die:
                            if m == j:
                                break
                        else:
                            continue

                        break
                    elif k == j:
                        for m in second_die:
                            if m == i:
                                break
                        else:
                            continue

                        break
                else:
                    break
            else:
                accumulate += 1

    return accumulate
