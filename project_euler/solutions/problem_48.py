def solve(bound: int=1000, modulo: int=10_000_000_000):
    return sum(pow(i, i, modulo) for i in range(1, bound + 1)) % modulo
