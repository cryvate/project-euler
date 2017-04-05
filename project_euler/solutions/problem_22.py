from os.path import join, split


def solve(file_path: str= 'problem_22_names.txt', relative: bool=True) -> int:
    if relative:
        full_path = join(split(__file__)[0], file_path)
    else:
        full_path = file_path
    with open(full_path, 'r') as names_file:
        names_raw = names_file.read()

    names = names_raw.strip('"').split('","')
    names = sorted(names)

    names_summed = [sum(ord(c) - ord('A') + 1 for c in name) for name in names]

    return sum((i + 1) * name_sum for i, name_sum in enumerate(names_summed))
