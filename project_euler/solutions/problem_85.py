from itertools import count


def solve(aim: int=2_000_000) -> int:
    closest = None
    area = None

    for i in count(1):
        for j in count(1):
            number = (i * (i + 1) * j * (j + 1)) // 4

            if closest is None or abs(number - aim) < closest:
                closest = abs(number - aim)
                area = i * j

            if number >= aim + closest:
                break

        if i >= aim + closest:
            break

    return area
