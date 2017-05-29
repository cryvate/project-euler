from itertools import chain, count, combinations_with_replacement, permutations

from ..framework.load_file import load_file


def solve(name: str= 'keylog.txt', relative: bool=True) -> str:
    constraints_raw = load_file(79, name, relative)

    constraints = [list(constraint)
                   for constraint in constraints_raw.split('\n')
                   if constraint != '']

    alphabet_set = set(chain(*constraints))
    alphabet = sorted(alphabet_set)

    for size in count(len(alphabet)):
        for combination in combinations_with_replacement(alphabet, size):
            if set(combination) != alphabet_set:
                continue

            for permutation in permutations(combination):
                for constraint in constraints:
                    reduced = [letter for letter in permutation
                               if letter in constraint]

                    for i, letter in enumerate(reduced):
                        if letter != constraint[1]:
                            continue

                        try:
                            reduced[:i].index(constraint[0])
                            reduced[i:].index(constraint[2])
                            break
                        except ValueError:
                            pass
                    else:
                        break

                    continue
                else:
                    return ''.join(permutation)
