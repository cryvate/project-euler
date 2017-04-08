import pytest

from .pythagorean_triples import primitive_pythagorean_triples

one_generation = [
    (5, 12, 13),
    lambda triplet, store=[True] * 4: store and store.pop(),
    [
        (5, 12, 13),
        (7, 24, 25),
        (55, 48, 73),
        (45, 28, 53),
    ]
]

second_biggest = (
    (3, 4, 5),
    lambda triplet, store=[True] * 4:
    triplet[0] < triplet[1] and store and store.pop(),
    [
        (3, 4, 5),
        (5, 12, 13),
        (7, 24, 25),
        (9, 40, 41),
    ]
)


@pytest.mark.parametrize('starting,valid,expected_output',
                         [one_generation, second_biggest])
def test_pythagorean_triples(starting, valid, expected_output) -> None:
    assert list(primitive_pythagorean_triples(valid, starting)) == \
           expected_output
