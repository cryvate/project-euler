from itertools import takewhile

from ..framework.load_file import load_file
from ..library.sequences import triangle_sequence


def solve(name: str= 'words.txt', relative: bool=True) -> int:
    words_raw = load_file(42, name, relative)

    words = words_raw.strip('"').split('","')
    value_words = [sum(ord(digit) - ord('A') + 1 for digit in word)
                   for word in words]
    max_value_words = max(value_words)

    triangle_numbers = list(takewhile(lambda n: n <= max_value_words,
                                      triangle_sequence()))

    return sum(1 for value in value_words if value in triangle_numbers)
