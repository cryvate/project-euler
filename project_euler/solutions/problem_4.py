def solve() -> int:
    highest = 0
    for b in range(999, 99, -1):
        if b * b < highest:
            break
        for a in range(b, 99, -1):
            if a * b < highest:
                break
            if str(a * b) == str(a * b)[::-1]:
                highest = a * b

    return highest
