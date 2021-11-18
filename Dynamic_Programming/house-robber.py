#!/usr/bin/python3
# https://leetcode.com/problems/house-robber/
from typing import List

"""
        0  1  2  3  4
       [2, 8, 3, 1, 10]

        base case if i < 0 return total
                                (0,i=4)
                                /    \
                             (10,i=2) (0,i=3)
                                        / \
                                    (1,i=1)(0, i=2)  

       return MAX    (10,i=2)=18                               (1,i=1)=9
                 /             \                           /        \
        (13,i=0)=15           (10,i=1)=18              (9,i=-1)=9     (1,i=0)=3
            /     \           /         \                            /     \
(15,i=-2)=15 (13,i=-1)=13 (18,i=-1)=18 (10,i=0)=12             (3,i=-2)=3  (1,i=-1)=1
                                      /       \
                               (12,i=-2)=12   (10,i=-1)=10

"""


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
