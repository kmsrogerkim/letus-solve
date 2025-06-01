def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

nums = [-1, 0, 2, 4, 6, 8]

print("Output for target 4:", binary_search(nums, 4))  # Output: 3
print("Output for target 3:", binary_search(nums, 3))  # Output: -1

