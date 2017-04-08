from ..library.number_theory.primes import prime_sieve, is_prime

from collections import OrderedDict
from typing import List, Tuple, Dict


def find_concatenatable_primes(ptuples: Dict[int, Dict[List[int], None]],
                               pairs: Dict[int, Dict[int, None]],
                               single: List[int]) -> \
        Tuple[Dict[int, Dict[List[int], None]],
              Dict[int, Dict[int, None]],
              List[int]]:
    ntuples = OrderedDict()

    for p in ptuples:
        for others in ptuples[p]:

            max_others = max(others)

            for q in single:
                if q <= max_others:
                    continue

                if (q, ) not in pairs[p]:
                    continue

                for r in others:
                    if pairs.get(r, None) is None or (q, ) not in pairs[r]:
                        break
                else:
                    if ntuples.get(p, None) is None:
                        ntuples[p] = OrderedDict.fromkeys([others + (q, )])
                    else:
                        ntuples[p][others + (q, )] = None

    primes_involved = []

    for p in ntuples:
        primes_involved.append(p)
        for others in ntuples[p]:
            primes_involved += others

    single = sorted(set(primes_involved))

    return ntuples, pairs, single


def solve(size: int=5) -> int:
    up_to = 10_000

    primes = [int(p) for p in prime_sieve(up_to)]
    pairs_up_to = up_to

    pairs = OrderedDict()

    def local_is_prime(n: int):
        if n > up_to:
            return is_prime(n, primes)
        return n in primes

    for i, p in enumerate(primes):
        if p > pairs_up_to:
            break
        for q in primes[i:]:
            if q > pairs_up_to:
                break

            if local_is_prime(int(str(p) + str(q))) and \
                    local_is_prime(int(str(q) + str(p))):
                if pairs.get(p, None) is None:
                    pairs[p] = OrderedDict.fromkeys([(q, )])
                else:
                    pairs[p][(q, )] = None

    some_primes = set()
    n_pairs = []
    for p in pairs:
        some_primes.add(p)
        for q in pairs[p]:
            some_primes.add(q[0])
            n_pairs.append((p, q[0]))

    singles = sorted(set(some_primes))

    i = 2
    ntuples = pairs
    pairs = pairs

    for i in range(3, size + 1):
        ntuples, pairs, singles = \
            find_concatenatable_primes(ntuples, pairs, singles)
        sums = []
        for p in ntuples:
            for others in ntuples[p]:
                sums.append((sum(others) + p, (p, ) + others))

        sums = sorted(sums)

    if sums[0][0] < up_to:
        print('This answer is guaranteed to be correct.')
    else:
        print('This answer is *NOT* guaranteed to be correct.')

    return sums[0][0]
