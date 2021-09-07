#!/usr/bin/python3
# https://leetcode.com/problems/two-sum/


def two_sum(nums, target):
    i, s = 0, len(nums)
    while i < s:
        r = target - nums[i]
        if r in nums:
            j = nums.index(r)
            if i != j:
                return [i, j]
        i += 1


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))

    # nums = [2, 7, 11, 15]
    # i = 2
    # print(nums[:i] + nums[i + 1:])

