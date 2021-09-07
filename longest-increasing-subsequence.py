#!/usr/bin/python3
# https://leetcode.com/problems/longest-increasing-subsequence/
from typing import List


# Dynamic Programming
# Time - O(n^2)
# Space - O(n)
def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)
    highestLength = 1
    maxLenArray = [1] * n
    for i in range(1, n):
        j = i - 1
        while j >= 0:
            if nums[i] > nums[j] and maxLenArray[i] <= maxLenArray[j]:
                maxLenArray[i] = maxLenArray[j] + 1
                if highestLength < maxLenArray[i]:
                    highestLength = maxLenArray[i]
            j -= 1
    return highestLength


if __name__ == '__main__':
    print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
    # print(lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4
    # print(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # 0
