from itertools import count


def digit_in_integers(n: int) -> int:
    if n <= 9:
        return n

    for level in count():
        if level == 0:
            continue

        if n >= 9 * (10 ** (level - 1)) * level:
            n -= 9 * (10 ** (level - 1)) * level
            continue

        number, position = divmod(n, level)

        return int(str(number + 10 ** (level - 1))[position - 1])


def solve() -> int:
    accumulate = 1

    for exp in range(6):
        accumulate *= digit_in_integers(10 ** exp)

    return accumulate
