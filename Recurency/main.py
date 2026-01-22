def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def sum_list_elements(arr):
    if not arr:
        return 0
    else:
        return arr[0] + sum_list_elements(arr[1:])


def count_list_elements(arr):
    if not arr:
        return 0
    else:
        return 1 + count_list_elements(arr[1:])


def find_max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


print(factorial(5))

l_example_values = [1, 2, 3, 4, 5]

print(sum_list_elements(l_example_values))
print(count_list_elements(l_example_values))
print(find_max(l_example_values))
