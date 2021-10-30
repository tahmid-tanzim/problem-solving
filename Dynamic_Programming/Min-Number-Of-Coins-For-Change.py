#!/usr/bin/python3
# https://www.algoexpert.io/questions/Min%20Number%20Of%20Coins%20For%20Change
"""
  Given an array of positive integers representing coin denominations and a
  single non-negative integer n representing a target amount of
  money, write a function that returns the smallest number of coins needed to
  make change for (to sum up to) that target amount using the given coin
  denominations.

  Note that you have access to an unlimited amount of coins. In other words, if
  the denominations are [1, 5, 10], you have access to an unlimited
  amount of 1s, 5s, and 10s.

  If it's impossible to make change for the target amount, return
  -1.
"""
import sys


# O(n) time, O(1) space
def minNumberOfCoinsForChange(n, denoms):
    numOfCoins = [sys.maxsize] * (n + 1)
    numOfCoins[0] = 0

    for coinValue in denoms:
        amount = coinValue
        while amount <= n:
            remainingAmount = amount - coinValue
            numOfCoins[amount] = min(numOfCoins[amount], 1 + numOfCoins[remainingAmount])
            amount += 1

    return numOfCoins[n] if numOfCoins[n] != sys.maxsize else -1


if __name__ == '__main__':
    # Output ~> 3 = 2x1 + 1x5
    print(minNumberOfCoinsForChange(7, [1, 5, 10]))
