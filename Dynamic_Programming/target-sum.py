#!/usr/bin/python3
# https://leetcode.com/problems/target-sum/
from typing import List
import time

"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of 
the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and 
concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
"""


# Brute Force
# O(2 ^ n) time, O(n) space
class Solution1:
    def __init__(self):
        self.numberOfWays = None

    def calculateWays(self, nums: List[int], target: int, index: int, total: int):
        if index < 0:
            if total == target:
                self.numberOfWays += 1
            return

        self.calculateWays(nums, target, index - 1, total + nums[index])
        self.calculateWays(nums, target, index - 1, total - nums[index])

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.numberOfWays = 0
        start = time.time()
        self.calculateWays(nums, target, len(nums) - 1, 0)
        end = time.time()
        print("Time - ", end - start)
        return self.numberOfWays


# Recursion with Memoization
# O(s * n) time, O(s * n) space
# s is the sum of nums
# n is the length of nums
class Solution2:
    def calculateWays(self, nums: List[int], target: int, index: int, total: int, DP_MEMO):
        if index < 0:
            if total == target:
                return 1
            else:
                return 0

        key = f"{index}:{total}"
        if key in DP_MEMO:
            return DP_MEMO[key]

        ADD = self.calculateWays(nums, target, index - 1, total + nums[index], DP_MEMO)
        SUBTRACT = self.calculateWays(nums, target, index - 1, total - nums[index], DP_MEMO)
        DP_MEMO[key] = ADD + SUBTRACT
        return DP_MEMO[key]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        DP_MEMO = dict()
        start = time.time()
        numberOfWays = self.calculateWays(nums, target, len(nums) - 1, 0, DP_MEMO)
        end = time.time()
        print("Time - ", end - start)
        return numberOfWays


# 2D Dynamic Programming
# O() time, O() space
class Solution3:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        pass


# 1D Dynamic Programming
# O() time, O() space
class Solution4:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        pass


if __name__ == "__main__":
    obj = Solution2()
    print(obj.findTargetSumWays([1, 1, 1, 1, 1], 3))  # 5
    print(obj.findTargetSumWays([1], 1))  # 1
