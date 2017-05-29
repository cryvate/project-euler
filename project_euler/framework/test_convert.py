import pytest

from .convert import convert


@pytest.mark.parametrize('string,converted', (('Foo', b'Rm9v'),
                                              ('Bar', b'QmFy')))
def test_convert(string, converted):
    assert convert(string) == converted
