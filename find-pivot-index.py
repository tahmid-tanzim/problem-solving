#!/usr/bin/python3
# https://leetcode.com/problems/find-pivot-index/
from typing import List


def pivotIndex(nums: List[int]) -> int:
    total = sum(nums)
    left_sum = 0
    for index in range(len(nums)):
        if left_sum == total - nums[index]:
            return index
        left_sum += nums[index]
        total -= nums[index]
    return -1


if __name__ == "__main__":
    print(pivotIndex([1, 7, 3, 6, 5, 6]) == 3)
    print(pivotIndex([1, 2, 3]) == -1)
    print(pivotIndex([2, 1, -1]) == 0)
    print(pivotIndex([-1, 1, 4]) == 2)
