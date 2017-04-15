from typing import Callable, List, Optional, Tuple

from ..library.base import number_to_list, list_to_number
from ..library.number_theory.primes import prime_sieve, is_prime

import numpy as np

Ntuples = Optional[List[List[int]]]
Pairs = Optional[List[List[bool]]]
Singles = List[int]
Representations = List[List[int]]


def compactify(ntuples: Ntuples,
               pairs: Pairs,
               singles: Singles,
               present: List[bool]) -> Tuple[Ntuples, Pairs, Singles]:
    length = len(singles)
    present_list = [i for i in range(length) if present[i]]
    transform = np.cumsum(present) -1

    singles = [singles[i] for i in present_list]
    pairs = [[pairs[i][j] for i in present_list] for j in present_list]

    ntuples = [[transform[i] for i in ntuple] for ntuple in ntuples]

    return ntuples, pairs, singles


def find_concatenatable_primes(ntuples: Ntuples,
                               pairs: Pairs,
                               singles: Singles) -> \
        Tuple[Ntuples, Pairs, Singles, Representations]:
    length = len(singles)

    present = [False] * length
    new_ntuples = []

    if pairs is None:
        pairs = [[False for j in range(length)] for i in range(length)]
        for i in range(1, length):
            p = singles[i]

            if p == 2:
                continue

            p_3 = p % 3
            rep_p = number_to_list(p)

            for j in range(i + 1, length):
                q = singles[j]
                rep_q = number_to_list(q)

                if ((q % 3) + p_3) % 3 == 0:
                    continue

                if not is_prime(int(str(p) + str(q)), singles):
                    continue

                if not is_prime(int(str(q) + str(p)), singles):
                    continue
                        #not is_prime(list_to_number(rep_p + rep_q), singles) or \
                        #not is_prime(list_to_number(rep_q + rep_p), singles):
                    continue

                new_ntuples.append([i, j])
                pairs[i][j] = True
                pairs[j][i] = True
                present[i] = True
                present[j] = True

        representations = [[singles[i] for i in ntuple] for ntuple in
                           new_ntuples]
        assert [3, 109] in representations
    else:
        for ntuple in ntuples:
            max_index = ntuple[-1]

            for valid, j in [(all(pairs[i][j] for i in ntuple), j) for j in range(max_index + 1, length)]:
                if valid:
                    new_ntuples.append(ntuple + [j])

                    present[j] = True
                    for i in ntuple:
                        present[i] = True

    old_representations = [[singles[i] for i in ntuple] for ntuple in
                           new_ntuples]

    new_ntuples, pairs, singles = compactify(new_ntuples, pairs, singles, present)

    representations = [[singles[i] for i in ntuple] for ntuple in new_ntuples]

    assert old_representations == representations

    return new_ntuples, pairs, singles, representations


def solve(size: int=5) -> int:
    up_to = 10_000

    ntuples = None
    pairs = None
    singles = prime_sieve(up_to)
    sums = singles
    index = 0

    print(f'using {len(singles)} primes.')

    for i in range(2, size + 1):
        ntuples, pairs, singles, representations = \
            find_concatenatable_primes(ntuples, pairs, singles)

        print(f'At size={i}, get {len(ntuples)} {i}-tuples')

        if i == 2:
            assert [3, 7] in representations
            assert [7, 109] in representations
            assert [3, 109] in representations
            assert [109, 673] in representations
            assert [7, 673] in representations
            assert [3, 673] in representations

        if i == 3:
            assert [3, 7, 109] in representations
            assert [7, 109, 673] in representations

        sums = [sum(representation) for representation in representations]

        try:
            index = sums.index(min(sums))
        except ValueError as e:
            raise ValueError(f'No solution for stage {i}, try a different '
                             f'value for up_to (currently {up_to}).') from e
        print(f'for size {i} we get best {representations[index]}')

    if sums[index] < up_to:
        print('This answer is guaranteed to be correct.')
    else:
        print('This answer is *NOT* guaranteed to be correct.')

    return sums[index]
