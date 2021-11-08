#!/usr/bin/python3
# https://leetcode.com/problems/combination-sum-iv/
from typing import List


# Recursive, Memoization
# O(t) time, O(t) space
class Solution1:
    def calculate(self, nums: List[int], target: int, CACHE) -> int:
        if target == 0:
            return 1
        if target < 0:
            return 0
        if target in CACHE:
            return CACHE[target]

        numberOfValidCombination = 0
        for n in nums:
            numberOfValidCombination += self.calculate(nums, target - n, CACHE)
        CACHE[target] = numberOfValidCombination
        return numberOfValidCombination

    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.calculate(nums, target, {})


if __name__ == "__main__":
    obj = Solution1()

    print(obj.combinationSum4([1, 2, 3], 4))
    # Output: 7
    # Explanation:
    # The possible combination ways are:
    # (1, 1, 1, 1)
    # (1, 1, 2)
    # (1, 2, 1)
    # (1, 3)
    # (2, 1, 1)
    # (2, 2)
    # (3, 1)
    # Note that different sequences are counted as different combinations.

    print(obj.combinationSum4([9], 3))
    # Output: 0
