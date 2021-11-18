#!/usr/bin/python3
# https://leetcode.com/problems/house-robber-ii/
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
        return max(nums[0], self.robHelper(nums[1:n], 0, n - 2), self.robHelper(nums[0:n - 1], 0, n - 2))


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
        if n <= 1:
            return nums[0]
        excludingFirstHouse = self.robHelper(nums[1:n], n - 2, {})
        excludingLastHouse = self.robHelper(nums[0:n - 1], n - 2, {})
        return max(excludingFirstHouse, excludingLastHouse)


if __name__ == '__main__':
    obj = Solution2()
    print(obj.rob([2, 3, 2]))  # 3
    print(obj.rob([1, 2, 3, 1]))  # 4
    print(obj.rob([1, 2, 3]))  # 3
