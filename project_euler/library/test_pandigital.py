from .pandigital import is_pandigital, is_pandigital_n


def test_is_pandigital() -> None:
    assert is_pandigital(1234567890, True)
    assert is_pandigital(123456789, False)

    assert not is_pandigital(123456789, True)
    assert not is_pandigital(1234567890, False)

    assert not is_pandigital(1234567899, False)


def test_is_pandigital_n() -> None:
    assert is_pandigital_n(123456789, 9)
    assert not is_pandigital_n(12345678, 9)
