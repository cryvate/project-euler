from os.path import join, split

from .problem_18 import solve as find_max_sum


def solve(file_path: str= 'problem_67_triangle.txt',
          relative: bool=True) -> int:
    if relative:
        full_path = join(split(__file__)[0], file_path)
    else:
        full_path = file_path
    with open(full_path, 'r') as triangle_file:
        triangle_raw = triangle_file.read()

    triangle = [[int(word.lstrip('0')) for word in line.split(' ')]
                for line in triangle_raw.split('\n') if line != '']

    return find_max_sum(triangle)
