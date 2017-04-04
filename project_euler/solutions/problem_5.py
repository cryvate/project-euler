from math import gcd


def solve(number: int=20) -> int:
    lcd = 1

    for i in range(1, number + 1):
        lcd = (lcd * i) // gcd(lcd, i)

    return lcd
