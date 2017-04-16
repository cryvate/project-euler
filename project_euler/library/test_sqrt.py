import pytest

from .sqrt import fsqrt, fast_fsqrt, csqrt, fast_csqrt, is_square, \
    is_square_fast


@pytest.mark.parametrize('n', range(100))
def test_sqrt(n: int) -> None:
    assert max(x for x in range(n + 1) if x * x <= n) == fsqrt(n)
    assert min(x for x in range(n + 1) if x * x >= n) == csqrt(n)

    assert max(x for x in range(n + 1) if x * x <= n) == fast_fsqrt(n)
    assert min(x for x in range(n + 1) if x * x >= n) == fast_csqrt(n)

@pytest.mark.parametrize('n', range(100))
def test_is_square(n: int) -> None:
    assert (fsqrt(n) == csqrt(n)) == is_square(n)
    assert (fsqrt(n) == csqrt(n)) == is_square_fast(n)
