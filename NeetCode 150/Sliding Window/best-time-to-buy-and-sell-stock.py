#!/usr/bin/python3
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


def maxProfit(prices: List[int]) -> int:
    """
    Time  - O(n^2)
    Space - O(1)
    """
    maximum_profit = 0
    n = len(prices)
    for buy in range(n - 1):
        for sell in range(buy + 1, n):
            profit = prices[sell] - prices[buy]
            if maximum_profit < profit:
                maximum_profit = profit
    return maximum_profit


def maxProfit2(prices: List[int]) -> int:
    """
    Time  - O(n)
    Space - O(1)
    """
    maximum_profit = 0
    n = len(prices)
    buy = 0
    sell = 1
    while sell < n:
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            if maximum_profit < profit:
                maximum_profit = profit
        else:
            buy = sell
        sell += 1
    return maximum_profit


if __name__ == '__main__':
    inputs = (
        {
            "prices": [7, 1, 5, 3, 6, 4],
            "expected": 5
        },
        {
            "prices": [7, 6, 4, 3, 1],
            "expected": 0
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = maxProfit(val["prices"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:   {output}\nExpected: {val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
