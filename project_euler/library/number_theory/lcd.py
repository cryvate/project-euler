from .gcd import gcd


def lcd(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)
