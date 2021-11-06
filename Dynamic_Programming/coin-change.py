#!/usr/bin/python3
# https://leetcode.com/problems/coin-change/
from typing import List

"""
You are given an integer array coins representing coins of different denominations and 
an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""


# O(A * n) time, O(A) space
# n is the number of coins
# A is the target amount
class Solution1:
    # Top Down, Recursive, Memoization (array)
    def coinChangeHelper(self, coins: List[int], remainingAmount: int, MEMOIZATION_TABLE) -> int:
        if remainingAmount < 0:
            return -1
        if remainingAmount == 0:
            return 0
        if MEMOIZATION_TABLE[remainingAmount - 1] is not None:
            return MEMOIZATION_TABLE[remainingAmount - 1]

        minResult = float("inf")
        for coin in coins:
            subResult = self.coinChangeHelper(coins, remainingAmount - coin, MEMOIZATION_TABLE)
            if 0 <= subResult < minResult:
                minResult = 1 + subResult
        if minResult == float("inf"):
            MEMOIZATION_TABLE[remainingAmount - 1] = -1
        else:
            MEMOIZATION_TABLE[remainingAmount - 1] = minResult
        return MEMOIZATION_TABLE[remainingAmount - 1]

    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChangeHelper(coins, amount, [None] * amount)


# O(A * n) time, O(A) space
# n is the number of coins
# A is the target amount
class Solution2:
    # Top Down, Recursive, Memoization (dictionary)
    def coinChangeHelper(self, coins: List[int], remainingAmount: int, MEMOIZATION_TABLE) -> int:
        if remainingAmount < 0:
            return -1
        if remainingAmount == 0:
            return 0
        if remainingAmount in MEMOIZATION_TABLE:
            return MEMOIZATION_TABLE[remainingAmount]

        minResult = float("inf")
        for coin in coins:
            subResult = self.coinChangeHelper(coins, remainingAmount - coin, MEMOIZATION_TABLE)
            if 0 <= subResult < minResult:
                minResult = 1 + subResult
        if minResult == float("inf"):
            MEMOIZATION_TABLE[remainingAmount] = -1
        else:
            MEMOIZATION_TABLE[remainingAmount] = minResult

        return MEMOIZATION_TABLE[remainingAmount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChangeHelper(coins, amount, dict())


# O(A * n) time, O(A) space
# n is the number of coins
# A is the target amount
class Solution3:
    # Bottom Up, Iterative, Tabulation
    def coinChange(self, coins: List[int], amount: int) -> int:
        numOfCoins = [float("inf")] * (amount + 1)
        numOfCoins[0] = 0
        for coinValue in coins:
            i = coinValue
            while i <= amount:
                remainingAmount = i - coinValue
                numOfCoins[i] = min(numOfCoins[i], 1 + numOfCoins[remainingAmount])
                i += 1
        return numOfCoins[amount] if numOfCoins[amount] != float("inf") else -1


if __name__ == "__main__":
    obj = Solution2()
    print(obj.coinChange([1, 2, 5], 11))  # 3
    print(obj.coinChange([2], 3))  # -1
    print(obj.coinChange([1], 0))  # 0
    print(obj.coinChange([1], 1))  # 1
    print(obj.coinChange([1], 2))  # 2
    print(obj.coinChange([186, 419, 83, 408], 6249))  # 20
