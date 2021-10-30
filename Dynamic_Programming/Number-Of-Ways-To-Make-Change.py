#!/usr/bin/python3
# https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Make%20Change
"""
  Given an array of distinct positive integers representing coin denominations and a
  single non-negative integer <span>n</span> representing a target amount of
  money, write a function that returns the number of ways to make change for
  that target amount using the given coin denominations.
"""


# O(nd) time, O(n) space
# n is the target amount & d is the number of coin denominations
def numberOfWaysToMakeChange(n, denoms):
    ways = [0] * (n + 1)
    ways[0] = 1

    for denom in denoms:
        i = denom
        while i <= n:
            ways[i] += ways[i - denom]
            i += 1

    return ways[-1]


if __name__ == '__main__':
    # Output ~> 2 = 1x1 + 1x5 and 6x1
    print(numberOfWaysToMakeChange(6, [1, 5]))
