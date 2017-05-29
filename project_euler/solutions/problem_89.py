import re

from ..framework.load_file import load_file


def solve(name: str='roman.txt', relative: bool=True) -> int:
    roman_raw = load_file(89, name, relative)

    shorter = 0

    numerals = [line for line in roman_raw.split('\n') if line]
    for numeral in numerals:
        length = len(numeral)

        numeral = re.sub('IIII', 'IV', numeral)
        numeral = re.sub('XXXX', 'XL', numeral)
        numeral = re.sub('CCCC', 'CD', numeral)
        numeral = re.sub('VIV', 'IX', numeral)
        numeral = re.sub('LXL', 'XC', numeral)
        numeral = re.sub('DCD', 'CM', numeral)

        shorter += length - len(numeral)

    return shorter
