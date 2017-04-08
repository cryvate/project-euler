def solve(max_n: int=100, at_least: int=1_000_000):
    counter = 0

    for n in range(1, max_n + 1):
        accumulate = 1

        for r in range(1, n // 2):
            accumulate = ((n + 1 - r) * accumulate) // r

            if accumulate >= at_least:
                counter += (n - 2 * r + 1)
                break

    return counter
