import pytest

from main import binary_search


@pytest.mark.parametrize("array, target, expected", [
    ([1, 3, 5, 7, 9, 11, 13, 15, 18], 15, 7),
    ([1, 3, 5, 7, 9, 11, 13, 15, 18], 5, 2),
    ([1, 3, 5, 7, 9, 11, 13, 15, 18], 99, None),
    ([], 15, None),
])
def test_binary_search(array: list[int], target:int, expected: int | None) -> None:
    assert binary_search(array, target) == expected
