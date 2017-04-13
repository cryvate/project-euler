def solve(depth: int=12_000) -> int:
    pre_rem_for_denominator = [0] * (depth + 1)
    count = 0

    for i in range(2, depth + 1):
        fractions_to_add = i - i // 2 - i // 3 - 1
        count += fractions_to_add
        numerators_to_remove = fractions_to_add - pre_rem_for_denominator[i]
        for j in range(i * 2, depth + 1, i):
            count -= numerators_to_remove
            pre_rem_for_denominator[j] += numerators_to_remove

    return count
