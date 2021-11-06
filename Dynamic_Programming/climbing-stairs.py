#!/usr/bin/python3
# https://leetcode.com/problems/climbing-stairs/


class Solution1:
    def climbStairs(self, n: int, memo: dict = {}) -> int:
        if n <= 1:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
        return memo[n]


class Solution2:
    @staticmethod
    def climbStairs(n: int) -> int:
        if n <= 1:
            return 1
        oneStep = 1
        twoStep = 1
        for step in range(2, n):
            temp = oneStep + twoStep
            oneStep = twoStep
            twoStep = temp
        return oneStep + twoStep


if __name__ == "__main__":
    s = Solution2()
    print(s.climbStairs(45))  # 1836311903
    # print(s.climbStairs(5))  # 3
