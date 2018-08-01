import itertools


def solve() -> int:
    total = 0

    for g00, g01 in itertools.product(range(0, 5), range(10)):
        for g02, g03 in itertools.product(range(0, g01 + 1), range(10)):
            s = g00 + g01 + g02 + g03

            for g10 in range(min(10, s + 1)):
                for g11 in range(min(10, s + 1 - g10)):
                    for g12 in range(min(10, s + 1 - g10 - g11)):
                        g13 = s - g10 - g11 - g12

                        if not (0 <= g13 <= 9):
                            continue

                        for g20 in range(min(10, s + 1 - g00 - g10)):
                            g30 = s - g00 - g10 - g20

                            if not (0 <= g30 <= 9):
                                continue

                            g21 = s - g03 - g12 - g30

                            if not (0 <= g21 <= 9):
                                continue

                            g31 = s - g01 - g11 - g21

                            if not (0 <= g31 <= 9):
                                continue

                            for g22 in range(min(10, s + 1 - g02 - g12)):
                                g32 = s - g02 - g12 - g22

                                if not (0 <= g32 <= 9):
                                    continue

                                g23 = s - g20 - g21 - g22

                                if not (0 <= g23 <= 9):
                                    continue

                                g33 = s - g03 - g13 - g23

                                if not (0 <= g33 <= 9):
                                    continue

                                if g20 + g21 + g22 + g23 != s:
                                    continue

                                if g30 + g31 + g32 + g33 != s:
                                    continue

                                if g00 + g11 + g22 + g33 != s:
                                    continue

                                total += 2 + 2 * (g02 < g01)

    return total
