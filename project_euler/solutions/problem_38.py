from ..library.pandigital import is_pandigital


def solve() -> int:
    maximum_found = 0

    for n in range(2, 5):
        for m in range(10 ** (9 // n), 0, -1):
            combined = int(''.join(str(k * m) for k in range(1, n + 1)))

            if combined <= maximum_found:
                break

            if is_pandigital(combined, False):
                maximum_found = combined

    return maximum_found
