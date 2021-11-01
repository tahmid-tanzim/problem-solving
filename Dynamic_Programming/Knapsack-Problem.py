#!/usr/bin/python3
# https://www.algoexpert.io/questions/Knapsack%20Problem
"""
  You're given an array of arrays where each subarray holds two integer values
  and represents an item; the first integer is the item's value, and the second
  integer is the item's weight. You're also given an integer representing the
  maximum capacity of a knapsack that you have.

  Your goal is to fit items in your knapsack without having the sum of their
  weights exceed the knapsack's capacity, all the while maximizing their
  combined value. Note that you only have one of each item at your disposal.

  Write a function that returns the maximized combined value of the items that
  you should pick as well as an array of the indices of each item picked.

  If there are multiple combinations of items that maximize the total value in
  the knapsack, your function can return any of them.

Sample Input
items = [[1, 2], [4, 3], [5, 6], [6, 7]]
capacity = 10

Sample Output
[10, [1, 3]] // items [4, 3] and [6, 7]
"""


def knapsack(items, itemIdx, capacity, memoize):
    if itemIdx < 0 or capacity < 0:
        return {
            "index": [],
            "value": 0
        }

    key = f'{itemIdx}-{capacity}'
    if key in memoize:
        return memoize[key]
    elif items[itemIdx][1] > capacity:
        # Don't Include in Bag
        memoize[key] = knapsack(items, itemIdx - 1, capacity, memoize)
        return memoize[key]
    else:
        itemIncluded = knapsack(items, itemIdx - 1, capacity - items[itemIdx][1], memoize)
        itemExcluded = knapsack(items, itemIdx - 1, capacity, memoize)
        include = {
            "index": itemIncluded["index"] + [itemIdx],
            "value": items[itemIdx][0] + itemIncluded["value"]
        }
        exclude = itemExcluded
        memoize[key] = include if include["value"] > exclude["value"] else exclude
        return memoize[key]


# O(nc) time | O(nc) space
# where n is the number of items and c is the capacity
def knapsackProblem(items, capacity):
    output = knapsack(items, len(items) - 1, capacity, {})
    return [output["value"], output["index"]]


if __name__ == "__main__":
    print(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10))
