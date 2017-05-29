from ..framework.load_file import load_file


def solve(name: str='names.txt', relative: bool=True) -> int:
    names_raw = load_file(22, name, relative)

    names = names_raw.strip('"').split('","')
    names = sorted(names)

    names_summed = [sum(ord(c) - ord('A') + 1 for c in name) for name in names]

    return sum((i + 1) * name_sum for i, name_sum in enumerate(names_summed))
