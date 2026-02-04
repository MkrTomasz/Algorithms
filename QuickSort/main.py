"""
QuickSort is a recursive, divide-and-conquer sorting algorithm.
In Python, it is commonly implemented using recursion and list slicing
or in-place partitioning.

The algorithm selects a pivot element (in below case it is the last element of the list),
then rearranges the list so that all elements smaller than the pivot come before it,
and all elements greater than the pivot come after it.
The pivot is then in its final sorted position.

QuickSort is recursively applied to the left and right sublists
until the entire list is sorted.

Average time complexity: O(n log n)
Worst-case time complexity: O(n^2)
Space complexity: O(log n) for recursion (in-place version)
"""


def quicksort(arr, low, high):
    if low < high:
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        pivot_index = i + 1

        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)
    return arr


def main() -> None:
    arr = [5, 3, 8, 4, 2, 7, 1, 10]
    low = 0
    high = len(arr) - 1
    print(f"QuickSort result: {quicksort(arr, low, high)}")


if __name__ == '__main__':
    main()
