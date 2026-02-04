import pytest

from main import quicksort


@pytest.mark.parametrize("arr, low, high, expected", [
    ([5, 3, 8, 4, 2, 7, 1, 10], 0, 7, [1, 2, 3, 4, 5, 7, 8, 10]),
    ([],0,0,[]),
])
def test_quicksort(arr: list[int], low: int, high: int, expected: list[int]) -> None:
    assert quicksort(arr, low, high) == expected
