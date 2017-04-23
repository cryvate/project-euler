from itertools import product
from math import gcd


def solve(bound: int=50) -> int:
    accumulate = 0

    # we are going to assume the right angle is at P and goes anti-clockwise
    # we need to multiply by 2 to get correct answer

    for x, y in product(range(bound + 1), range(bound + 1)):
        if x == 0 and y == 0:
            continue

        common = gcd(x, y)

        step_x, step_y = y // common, x // common

        steps_allowed_x = x // step_x if step_x else bound
        steps_allowed_y = (bound - y) // step_y if step_y else bound

        steps_allowed = min(steps_allowed_x, steps_allowed_y)
        print((x, y), steps_allowed)
        accumulate += steps_allowed

    accumulate *= 2  # also allow for right angle anti-clockwise
    accumulate += bound * bound  # right angle at O

    return accumulate
