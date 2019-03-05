def remove_duplicates(nums):
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == nums[i - 1]:
            del nums[i]
    return len(nums)


print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
