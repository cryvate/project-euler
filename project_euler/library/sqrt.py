def fsqrt(n: int) -> int:
    xs = [-2, -2, n]

    if n == 0:
        return 0

    if n < 0:
        raise ValueError(f'Cannot take square root of negative number {n}.')

    while True:
        xs = xs[1], xs[2], (xs[2] + n // xs[2]) // 2

        if xs[1] == xs[2]:
            return xs[1]
        if xs[0] == xs[2] and xs[1] == xs[0] + 1:
            return xs[0]


def csqrt(n: int) -> int:
    approx = fsqrt(n)

    return approx if approx * approx == n else approx + 1


def is_square(n: int) -> bool:
    return fsqrt(n) ** 2 == n


def is_square_fast(n: int) -> bool:
    return int(n ** 0.5) ** 2 == n
