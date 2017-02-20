import pytest


from .lcd import lcd


@pytest.mark.parametrize('a,b,answer', ((1, 1, 1), (2, 3, 6), (20, 10, 20),
                         (10, 15, 30)))
def test_lcd(a: int, b: int, answer: int) -> None:
    assert lcd(a, b) == answer
