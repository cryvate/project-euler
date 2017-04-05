def solve() -> int:
    accumulate = -1  # don't count 1.

    for i in range(1, 1_000_000):
        print(i)
        sum_powers = sum(int(digit) ** 5 for digit in str(i))

        if sum_powers == i:
            accumulate += i

    return accumulate
