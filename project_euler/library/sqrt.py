def fsqrt(n: int) -> int:
    xs = [-2, -2, n]

    while True:
        xs = xs[1], xs[2], (xs[2] + n // xs[2]) // 2

        if xs[1] == xs[2]:
            return xs[1]
        if xs[0] == xs[2] and xs[1] == xs[0] + 1:
            return xs[0]


def csqrt(n: int) -> int:
    approx = fsqrt(n)

    return approx + (0 if approx * approx == n else 1)
