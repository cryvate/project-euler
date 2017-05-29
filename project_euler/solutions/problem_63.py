from itertools import count


def solve() -> int:
    counter = 0

    for digits in count(1):
        if 9 ** digits < 10 ** (digits - 1):
            break

        for base in range(9, 0, -1):
            if base ** digits >= 10 ** (digits - 1):
                counter += 1
            else:
                break

    return counter
