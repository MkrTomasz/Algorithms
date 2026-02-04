import pytest

from main import selection_sort


@pytest.mark.parametrize("arr, expected", [
    ([64, 25, 12, 22, 11], [11, 12, 22, 25, 64]),
    ([15, -7, 30 ,1], [-7, 1, 15, 30]),
    ([], []),
    ([1], [1]),
])
def test_selection_sort(arr: list[int], expected: list[int]) -> None:
    assert selection_sort(arr) == expected
