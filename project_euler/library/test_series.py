import pytest

from project_euler.library import series as series_module

series_dict = {}
reference_values = {
    'fibonacci': [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
    'primes_nomemory': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
}

for attribute in dir(series_module):
    if attribute.endswith("_series"):
        series_dict[attribute[:-7]] = getattr(series_module, attribute)


@pytest.mark.parametrize("series_name", series_dict)
def test_series(series_name: str):
    series = series_dict[series_name]()

    try:
        reference_series = reference_values[series_name]
    except KeyError as e:
        raise NoReferenceException(f'No reference values provided for '
                                   f'{series_name} series.') from e

    for i, (calculated, reference) in enumerate(zip(series, reference_series)):
        try:
            assert calculated == reference
        except AssertionError as e:
            raise ValueException(f"Calculcated value and reference value on "
                                 f"{series_name} series do not agree at "
                                 f"index {i}: {calculated} and "
                                 f"{reference} repsectively.") from e


class ValueException(Exception):
    pass


class NoReferenceException(Exception):
    pass
