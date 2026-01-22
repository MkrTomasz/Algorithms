def two_sum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        y = target - nums[i]

        if y in hashmap:
            return hashmap[y], i

        hashmap[nums[i]] = i

arr = [5, 3, 8, 4, 2, 7, 1, 10]
print(two_sum(arr, 8))