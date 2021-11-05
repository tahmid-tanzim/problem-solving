#!/usr/bin/python3
# https://leetcode.com/problems/min-cost-climbing-stairs/
from typing import List

"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""


# O(n) time, O(1) space
class Solution1:
    # Top Down, Recursive
    def minCostClimbingStairsHelper(self, cost: List[int], index, totalCost) -> int:
        if index < 2:
            return cost[index]

        previousOneStepCost = self.minCostClimbingStairsHelper(cost, index - 1, totalCost)
        previousTwoStepCost = self.minCostClimbingStairsHelper(cost, index - 2, totalCost)
        currentStepCost = 0 if index == len(cost) else cost[index]
        totalCost += min(previousOneStepCost, previousTwoStepCost) + currentStepCost
        return totalCost

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        return self.minCostClimbingStairsHelper(cost, n, 0)


# O(n) time, O(1) space
class Solution2:
    # Bottom Up, Iterative
    @staticmethod
    def minCostClimbingStairs(cost: List[int]) -> int:
        n = len(cost)
        first, second, *others = cost

        for i in range(2, n):
            temp = cost[i] + min(first, second)
            first = second
            second = temp

        return min(first, second)


if __name__ == "__main__":
    obj = Solution2()
    print(obj.minCostClimbingStairs([10, 15, 20]))  # 15
    print(obj.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
    print(obj.minCostClimbingStairs([0, 2, 2, 1]))  # 2
