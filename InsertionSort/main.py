"""
Insertion Sort is a simple, comparison-based sorting algorithm.
In Python, it is typically implemented using loops and in-place updates.

The algorithm builds the sorted list one element at a time by taking
each element and inserting it into its correct position among the
previously sorted elements.

For each iteration, the current element is compared with elements
to its left and shifted leftward until it reaches its proper position.

Insertion Sort is efficient for small datasets or nearly sorted lists.

Average time complexity: O(n^2)
Worst-case time complexity: O(n^2)
Best-case time complexity: O(n) for already sorted input
Space complexity: O(1)
"""

def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def main() -> None:
    arr = [8, 7, 2, 80, 15, 0, -10, 1]
    print(f"Insertion sort result: {insertion_sort(arr)}")


if __name__ == '__main__':
    main()
