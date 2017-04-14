from ..library.partitions import partitions


def solve(index: int=100) -> int:
    return partitions(index) - 1
