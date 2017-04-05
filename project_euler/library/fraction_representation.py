from fractions import Fraction

from typing import List, Tuple


Representation = Tuple[Tuple[int, int], Tuple[int, int]]


def unit_fraction_to_representation(denominator: int,
                                    base: int=10) -> Representation:
    return fraction_to_representation(Fraction(1, denominator), base)


def fraction_to_representation(fraction: Fraction,
                               base: int=10) -> Representation:
    """Returns fraction representation of 1 / denominator as

     0.abcd(efgh)

     as

     ((abcd, 4), (efgh, 4))."""
    if fraction < 0 or fraction >= 1:
        raise ValueError(f'Cannot find decimal expansion of {fraction}, '
                         f' require 0 <= x < 1.')

    numerator = fraction.numerator
    denominator = fraction.denominator

    block_size = 1
    block_length = 0

    while block_size < denominator:
        block_size *= base
        block_length += 1

    remainders = []
    blocks = []
    remainder = block_size * numerator

    while (remainder not in remainders) and remainder != 0:
        remainders.append(remainder)

        block, remainder = divmod(remainder, denominator)

        blocks.append(block)

        remainder *= block_size

    if remainder == 0:  # terminating
        index = len(remainders)
    else:  # repeating
        index = remainders.index(remainder)

    def join_blocks(blocks: List[List[int]]) -> Tuple[List[int], int]:
        length = 0
        accumulate = 0

        for block in blocks:
            length += block_length

            accumulate *= block_size
            accumulate += block

        return accumulate, length

    prefix = join_blocks(blocks[:index])
    repeat = join_blocks(blocks[index:])

    return prefix, repeat


def representation_to_fraction(representation: Representation,
                               base: int=10) -> Fraction:
    prefix_factor = base ** representation[0][1]

    if representation[1][1] == 0:
        return Fraction(representation[0][0], prefix_factor)

    geometric = base ** representation[1][1] - 1
    numerator = representation[0][0] * geometric + representation[1][0]

    return Fraction(numerator, prefix_factor * geometric)
