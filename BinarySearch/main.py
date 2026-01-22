"""
Binary search is a fast way to find something in a sorted list by repeatedly cutting the list in half.

How it works:
1. Look at the middle item in the list.
2. If it’s what you want, you’re done.
3. If your item is smaller, ignore the right half.
4. If your item is bigger, ignore the left half.
5. Repeat with the remaining half until you find it (or it’s not there).

Example:
If you’re looking for the number 15 in this sorted list:
[1, 3, 5, 7, 9, 11, 13, 15, 18]
You check the middle (9), target is higher so 9 becomes the new low, again check middle (13),
target is higher so 13 becomes the new low, again check the middle (15), which is matching the target.

Time complexity:
Worst case: O(log n)
Best case: O(1) (the middle item is the target)
Average case: O(log n)

Space complexity:
O(1)
"""

def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(binary_search(my_array, 15))
print(binary_search(my_array, 7))
print(binary_search(my_array, 99))
print(binary_search(my_array, -1))
