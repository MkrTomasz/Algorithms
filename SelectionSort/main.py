def get_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_index = get_smallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr


array_to_be_sorted = [3, 5, 4, 2, 1]

print(selection_sort(array_to_be_sorted))