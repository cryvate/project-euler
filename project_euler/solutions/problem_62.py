from collections import Counter
from itertools import count

from ..library.sequences import cube_sequence, find_intersection_interval
from ..library.base import number_to_list


def solve(perms: int=5) -> int:
    for size in count(0):
        cubes = find_intersection_interval(cube_sequence(),
                                           begin=10 ** size,
                                           end=10 ** (size + 1))

        counter = Counter()

        for cube in cubes:
            counter[tuple(sorted(number_to_list(cube)))] += 1

        if perms in counter.values():
            cubes = find_intersection_interval(cube_sequence(),
                                               begin=10 ** size,
                                               end=10 ** (size + 1))

            valid = []

            for cube in cubes:
                if counter[tuple(sorted(number_to_list(cube)))] == perms:
                    cubes = find_intersection_interval(cube_sequence(),
                                                       begin=10 ** size,
                                                       end=10 ** (size + 1))
                    return cube
