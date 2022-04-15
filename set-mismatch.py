#!/usr/bin/python3
# https://leetcode.com/problems/set-mismatch/
from typing import List


def findErrorNums(nums: List[int]) -> List[int]:
    mismatch = [None, None]
    frequency = [0] * len(nums)
    for num in nums:
        frequency[num - 1] += 1

        if frequency[num - 1] == 2:
            mismatch[0] = num
    mismatch[1] = frequency.index(0) + 1
    return mismatch


if __name__ == "__main__":
    print(findErrorNums([1, 2, 2, 4]))  # [2, 3]
    print(findErrorNums([1, 1]))  # [1, 2]
    print(findErrorNums([1, 2, 3, 4, 3]))  # [3, 5]
    print(findErrorNums([1, 2, 2]))  # [2, 3]
    print(findErrorNums([3, 2, 2]))  # [2, 1]
    print(findErrorNums([3, 2, 3, 4, 6, 5]))  # [3, 1]
