import pytest

from main import insertion_sort


@pytest.mark.parametrize("arr, expected", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([2, 1, 4, 5, 3], [1, 2, 3, 4, 5]),
    ([80, -20, 73, 1, 15, 0, 62], [-20, 0, 1, 15, 62, 73, 80]),
    ([], []),
])
def test_insertion_sort(arr: list[int], expected: list[int]) -> None:
    assert insertion_sort(arr) == expected
