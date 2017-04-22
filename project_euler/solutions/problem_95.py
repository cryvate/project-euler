from ..library.number_theory.divisors import divisor_range


def solve(bound: int=1_000_000):
    chains_with_length = [None for _ in range(bound + 1)]
    divisor_sum = divisor_range(bound)

    chains_with_length[0] = (1, [0])

    for i in range(1, bound + 1):
        if chains_with_length[i] is not None:
            continue

        hit = [i]

        n = divisor_sum[i] - i

        while n <= bound and chains_with_length[n] is None and n not in hit:
            hit.append(n)
            n = divisor_sum[n] - n

        if n > bound:
            for n in hit:
                chains_with_length[n] = (0, [])

        if n in hit:
            chain = hit[hit.index(n):]
            chain_with_length = (len(chain), chain)
            for n in hit:
                chains_with_length[n] = chain_with_length
        else:
            chain_with_length = chains_with_length[n]
            chain_elements = chain_with_length[1]

            for n in hit:
                if hit in chain_elements:
                    break

                chains_with_length[n] = chain_with_length

    return min(max(chains_with_length)[1])
