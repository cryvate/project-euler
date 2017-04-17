from os.path import join, split

DIRECTORY = join(split(__file__)[0], '..', 'data', 'problems')


def load_file(problem_number: int, name: str, relative: bool=True) -> str:
    if relative:
        full_path = join(DIRECTORY, f'{problem_number}_{name}')
    else:
        full_path = name

    with open(full_path, 'r') as file:
        return file.read()
