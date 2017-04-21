from math import log

from ..framework.load_file import load_file


def solve(name: str='base_exp.txt', relative: bool=True) -> int:
    raw = load_file(99, name, relative)

    log_size = []

    for line in raw.split('\n'):
        if not line:
            continue

        base, exp = [int(n) for n in line.split(',')]

        log_size.append(exp * log(base))

    return log_size.index(max(log_size)) + 1
