def contribution(level: int) -> int:
    if level == 0:
        return 1

    return 4 * (2 * level + 1) ** 2 - (2 * level) * (3 * 4 // 2)


def solve(layers: int=1001) -> int:
    if layers % 2 == 0:
        raise ValueError(f'Require an odd number of layers, not {layers}')

    return sum(contribution(level) for level in range(layers // 2 + 1))
