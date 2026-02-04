import pytest

from main import fib_fast, fib_recursive


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (5, 5),
    (10, 55),
    (30, 832040),
    (100, 354224848179261915075),
])
def test_fib(n: int, expected: int) -> None:
    assert fib_fast(n) == expected


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (5, 5),
    (10, 55),
    (30, 832040),
])
def test_fib_recursive(n: int, expected: int) -> None:
    assert fib_recursive(n) == expected
