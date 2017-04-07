from os.path import join, split

from itertools import takewhile

from ..library.sequences import triangle_sequence


def solve(file_path: str= 'problem_42_words.txt', relative: bool=True) -> int:
    if relative:
        full_path = join(split(__file__)[0], file_path)
    else:
        full_path = file_path
    with open(full_path, 'r') as words_file:
        words_raw = words_file.read()

    words = words_raw.strip('"').split('","')
    value_words = [sum(ord(digit) - ord('A') + 1 for digit in word)
                   for word in words]
    max_value_words = max(value_words)

    triangle_numbers = list(takewhile(lambda n: n <= max_value_words,
                                      triangle_sequence()))

    return sum(1 for value in value_words if value in triangle_numbers)
