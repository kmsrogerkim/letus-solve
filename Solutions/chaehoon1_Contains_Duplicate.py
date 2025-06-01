def containsDuplicate(nums):
    return len(nums) != len(set(nums))

nums = [1, 1, 2, 3]
nums2 = [2, 3, 4]

print(containsDuplicate(nums))
print(containsDuplicate(nums2))
