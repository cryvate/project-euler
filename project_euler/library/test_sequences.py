import pytest

from project_euler.library import sequences as sequence_module

sequences_dict = {}
reference_values = {
    'fibonacci': [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
    'primes': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
    'collatz': [13, 40, 20, 10, 5, 16, 8, 4, 2, 1],
    'triangle': [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55],
    'square': [0, 1, 4, 9, 16, 25],
    'pentagonal': [0, 1, 5, 12, 22, 35, 51, 70, 92, 117, 145],
    'hexagonal': [0, 1, 6, 15, 28, 45],
    'heptagonal': [0, 1, 7, 18, 34, 55],
    'octagonal': [0, 1, 8, 21, 40, 65],
}

for attribute in dir(sequence_module):
    if attribute.endswith('_sequence') and not attribute.startswith('create'):
        sequences_dict[attribute[:-9]] = getattr(sequence_module, attribute)


class ValueException(Exception):
    pass


class NoReferenceException(Exception):
    pass


@pytest.mark.parametrize('sequence_name', sequences_dict)
def test_sequence(sequence_name: str):
    sequence = sequences_dict[sequence_name]()

    try:
        reference_sequence = reference_values[sequence_name]
    except KeyError as e:
        raise NoReferenceException(f'No reference values provided for '
                                   f'{sequence_name} sequence.') from e

    for i, (calculated, reference) in enumerate(zip(sequence,
                                                    reference_sequence)):
        try:
            assert calculated == reference
        except AssertionError as e:
            raise ValueException(f"Calculcated value and reference value on "
                                 f"{sequence_name} sequence do not agree at "
                                 f"index {i}: {calculated} and "
                                 f"{reference} repsectively.") from e


def test_find_intersection_interval():
    find_intersection_interval = sequence_module.find_intersection_interval
    input = [-1, 0, 1, 2, 3, 2, 1]
    assert list(find_intersection_interval(input, begin=0, end=2)) == [0, 1]
    assert list(find_intersection_interval(input,
                                           begin=0,
                                           end=2,
                                           breaking=False)) == [0, 1, 1]
