from .pandigital import is_pandigital


def test_pandigital() -> None:
    assert is_pandigital(1234567890, True)
    assert is_pandigital(123456789, False)

    assert not is_pandigital(123456789, True)
    assert not is_pandigital(1234567890, False)

    assert not is_pandigital(1234567899, False)
