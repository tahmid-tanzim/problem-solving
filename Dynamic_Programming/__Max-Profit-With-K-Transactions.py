#!/usr/bin/python3
# https://www.algoexpert.io/questions/Max%20Profit%20With%20K%20Transactions
"""
  You're given an array of positive integers representing the prices of a single stock on
  various days (each index in the array represents a different day). You're also
  given an integer k, which represents the number of transactions
  you're allowed to make. One transaction consists of buying the stock on a
  given day and selling it on another, later day.

  Write a function that returns the maximum profit that you can make by buying
  and selling the stock, given k transactions.

  Note that you can only hold one share of the stock at a time; in other words,
  you can't buy more than one share of the stock on any given day, and you can't
  buy a share of the stock if you're still holding another share. Also, you
  don't need to use all k transactions that you're allowed.

Sample Input
prices = [5, 11, 3, 50, 60, 90]
k = 2

Sample Output
93 // Buy: 5, Sell: 11; Buy: 3, Sell: 90
"""


def findMaxProfit(prices, buyIndx, n, transactionCount, memoize):
    # Base Case
    if transactionCount <= 0 or buyIndx >= n:
        return {"value": 0, "index": buyIndx, "k": transactionCount}

    key = f'{buyIndx}-{transactionCount}'
    if key in memoize:
        return memoize[key]

    maxProfit = 0
    for sellIdx in range(buyIndx + 1, n):
        if prices[sellIdx] > prices[buyIndx]:
            currentProfit = prices[sellIdx] - prices[buyIndx]
            futureProfit = findMaxProfit(prices, sellIdx + 1, n, transactionCount - 1, memoize)
            if maxProfit < currentProfit + futureProfit["value"]:
                maxProfit = currentProfit + futureProfit["value"]

    memoize[key] = {"value": maxProfit, "index": buyIndx, "k": transactionCount}
    return memoize[key]


# O(nk) time | O(n) space
# where n is the number of prices and k is the number of transactions
def maxProfitWithKTransactions(prices, k):
    n = len(prices)
    profit = list()
    output = findMaxProfit(prices, 0, n, k, {})
    profit.append(output["value"])
    print(output)
    while output["index"] < n and output["k"] > 0:
        output = findMaxProfit(prices, output["index"] + 1, n, output["k"], {})
        print(output)
        profit.append(output["value"])
    return max(profit)


if __name__ == '__main__':
    print(maxProfitWithKTransactions([5, 11, 3, 50, 60, 90], 2))
