from math import log10, sqrt


def solve(log10_above: int=999) -> int:
    golden_ratio = (1 + sqrt(5)) / 2

    return round((log10_above + log10(sqrt(5))) / log10(golden_ratio))
