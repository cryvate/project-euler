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
    print(digit_in_integers(12))
    print(list(digit_in_integers(x) for x in range(1, 30)))
    for exp in range(6):
        accumulate *= digit_in_integers(10 ** exp)

    return accumulate
