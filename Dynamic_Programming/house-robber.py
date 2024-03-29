#!/usr/bin/python3
# https://leetcode.com/problems/house-robber/
from typing import List


# Top Down, Recursive
# Time - O(2^n), Space - O(2^n)
class Solution1:
    def robHelper(self, nums: List[int], totalMoney: int, houseIndex: int) -> int:
        if houseIndex < 0:
            return totalMoney

        INCLUDE_MONEY = self.robHelper(nums, totalMoney + nums[houseIndex], houseIndex - 2)
        EXCLUDE_MONEY = self.robHelper(nums, totalMoney, houseIndex - 1)
        return max(INCLUDE_MONEY, EXCLUDE_MONEY)

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return self.robHelper(nums, 0, n - 1)


# Top Down, Recursive, Memoization
# Time - O(n), Space - O(n)
class Solution2:
    def robHelper(self, nums: List[int], houseIndex: int, cache: dict) -> int:
        if houseIndex < 0:
            return 0
        if houseIndex in cache:
            return cache[houseIndex]
        INCLUDE_MONEY = nums[houseIndex] + self.robHelper(nums, houseIndex - 2, cache)
        EXCLUDE_MONEY = self.robHelper(nums, houseIndex - 1, cache)
        cache[houseIndex] = max(INCLUDE_MONEY, EXCLUDE_MONEY)
        return cache[houseIndex]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return self.robHelper(nums, n - 1, {})


# Bottom Up, Tabulation
# Time - O(n), Space - O(n)
class Solution3:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        TABLE = [0] * (n + 1)
        TABLE[1] = nums[0]
        for houseIndex in range(2, n + 1):
            TABLE[houseIndex] = max(TABLE[houseIndex - 1], TABLE[houseIndex - 2] + nums[houseIndex - 1])
        return TABLE[n]


if __name__ == '__main__':
    obj = Solution3()
    print(obj.rob([1, 2, 3, 1]))  # 4
    print(obj.rob([2, 7, 9, 3, 1]))  # 12
    print(obj.rob([2, 8, 3, 1, 10]))  # 18
    print(obj.rob([10]))  # 10
    print(obj.rob([18, 100]))  # 100
