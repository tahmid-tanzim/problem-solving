#!/usr/bin/python3
# https://leetcode.com/problems/minimum-cost-for-tickets/
from typing import List

"""
You have planned some train traveling one year in advance. 
The days of the year in which you will travel are given as an integer array days. 
Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

~> a 1-day pass is sold for costs[0] dollars,
~> a 7-day pass is sold for costs[1] dollars, and
~> a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

~> For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.
"""


# O(n) time, O(1) space
class Solution1:
    def minCostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = dict()

        def dfs(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = float("inf")
            for day, cost in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + day:
                    j += 1
                dp[i] = min(dp[i], cost + dfs(j))

            return dp[i]

        return dfs(0)


class Solution2:
    def minCostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = dict()
        for i in range(len(days) - 1, -1, -1):
            dp[i] = float("inf")
            for day, cost in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + day:
                    j += 1
                dp[i] = min(dp[i], cost + dp.get(j, 0))
        return dp[0]


if __name__ == "__main__":
    obj = Solution2()
    print(obj.minCostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))  # 11
    print(obj.minCostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))  # 17
