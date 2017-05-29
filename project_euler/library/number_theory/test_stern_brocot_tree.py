from fractions import Fraction

import pytest

from .stern_brocot_tree import mediant, stern_brocot_tree, \
    size_stern_brocot_tree

MEDIANTS = [
    (Fraction(0), Fraction(1), Fraction(1, 2)),
    (Fraction(1), Fraction(3, 2), Fraction(4, 3)),
    (Fraction(3, 2), Fraction(1), Fraction(4, 3)),
]

STERN_BROCOT_TREE = [
    Fraction(1, 2), Fraction(1, 3), Fraction(2, 3), Fraction(1, 4),
    Fraction(2, 5), Fraction(3, 5), Fraction(3, 4), Fraction(1, 5),
    Fraction(2, 7), Fraction(3, 8), Fraction(3, 7), Fraction(4, 7),
    Fraction(5, 8), Fraction(5, 7), Fraction(4, 5), Fraction(1, 6),
    Fraction(5, 6), Fraction(1, 7), Fraction(6, 7), Fraction(1, 8),
    Fraction(7, 8)
]


@pytest.mark.parametrize('left,right,expected_output', MEDIANTS)
def test_mediant(left: Fraction, right: Fraction, expected_output: Fraction) \
        -> None:
    assert mediant(left, right) == expected_output


def test_stern_brocot_tree(depth: int=8) -> None:
    def classifier(fraction: Fraction) -> bool:
        return fraction.denominator <= depth

    tree_depth = list(stern_brocot_tree(depth=depth))
    tree_classifier = list(stern_brocot_tree(classifier=classifier))

    fractions = set()

    for n in range(2, depth + 1):
        for m in range(1, n):
            fractions.add(Fraction(m, n))

    assert set(tree_depth) == fractions
    assert set(tree_classifier) == fractions


@pytest.mark.parametrize('depth', range(5, 10))
def test_size_stern_brocot_tree(depth: int) -> None:
    assert len(list(stern_brocot_tree(depth=depth))) == \
           size_stern_brocot_tree(depth)
