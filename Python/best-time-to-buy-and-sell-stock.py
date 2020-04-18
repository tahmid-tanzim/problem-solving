#!/usr/local/bin/python3.6
import sys


def max_profit(prices):
    maximum_profit = 0
    minimum_price = sys.maxsize
    for price in prices:
        if price < minimum_price:
            minimum_price = price
        elif price - minimum_price > maximum_profit:
            maximum_profit = price - minimum_price
    return maximum_profit


if __name__ == '__main__':
    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([7, 6, 4, 3, 1]))
