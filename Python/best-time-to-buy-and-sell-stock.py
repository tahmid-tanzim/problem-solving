#!/usr/local/bin/python3.6
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii


def maxProfit(prices):
    max_profit, i = 0, 1
    price = {'min': prices[0], 'max': 0}
    while i < len(prices):
        if prices[i] <= price['min'] and price['max'] == 0:
            price['min'] = prices[i]
        elif prices[i] >= price['max']:
            price['max'] = prices[i]
        else:
            max_profit += price['max'] - price['min']
            price = {'min': prices[i], 'max': 0}
        i += 1
    if price['max'] > price['min']:
        max_profit += price['max'] - price['min']
    return max_profit


if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))  # 7
    print(maxProfit([1, 2, 3, 4, 5]))  # 4
    print(maxProfit([7, 6, 4, 3, 1]))  # 0
    print(maxProfit([2, 4, 1]))  # 2
