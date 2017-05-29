from ..framework.load_file import load_file

from .problem_18 import solve as find_max_sum


def solve(name: str= 'triangle.txt', relative: bool=True):
    triangle_raw = load_file(67, name, relative)

    triangle = [[int(word.lstrip('0')) for word in line.split(' ')]
                for line in triangle_raw.split('\n') if line != '']

    return find_max_sum(triangle)
