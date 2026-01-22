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


data = [5, 3, 8, 4, 2, 7, 1, 10]
quicksort(data, 0, len(data) - 1)
print(data)