"""
Selection Sort is a simple, comparison-based sorting algorithm.
In Python, it is usually implemented using nested loops and
in-place element swapping.

The algorithm divides the list into a sorted and an unsorted part.
It repeatedly selects the smallest element from the unsorted part
and swaps it with the first element of that part.

With each iteration, the sorted portion of the list grows,
while the unsorted portion shrinks.

Selection Sort performs the same number of comparisons regardless
of the initial order of elements.

Time complexity:
- Best-case: O(n^2)
- Average-case: O(n^2)
- Worst-case: O(n^2)

Space complexity: O(1)
"""


def selection_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def main() -> None:
    arr = [64, 25, 12, 22, 11]
    print(f"Selection sort result: {selection_sort(arr)}")

if __name__ == "__main__":
    main()
