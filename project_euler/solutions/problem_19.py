def zellers_congruence(day: int, month: int, year: int) -> int:
    '''see https://en.wikipedia.org/wiki/Zeller%27s_congruence'''
    q = day

    m = month + 1
    if month == 0 or month == 1:
        m += 12

    K = year % 100
    J = year // 100

    h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7

    return h


def solve(begin: int=1901, end: int=2000) -> str:
    mondays = 0
    for year in range(begin, end + 1):
        for month in range(12):
            mondays += zellers_congruence(1, month, year) == 1

    return str(mondays)
