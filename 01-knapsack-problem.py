#!/usr/local/bin/python3
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# https://www.youtube.com/watch?v=fJbIuhs24zQ
"""
# Dynamic Programming
# 0/1 Knapsack
# Memoization
"""


# def knapsack(value: list, weight: list, w: int, n: int) -> int:
#     # print(w, n, t)
#     if w == 0 or n == 0:
#         return 0
#
#     if t[n][w] != -1:
#         return t[n][w]
#
#     if weight[n - 1] <= w:
#         include = value[n - 1] + knapsack(value, weight, w - weight[n - 1], n - 1)
#         discard = knapsack(value, weight, w, n - 1)
#         t[n][w] = max(include, discard)
#         return t[n][w]
#     elif weight[n - 1] > w:
#         discard = knapsack(value, weight, w, n - 1)
#         t[n][w] = discard
#         return t[n][w]


def knapsack(value: list, weight: list, w: int, n: int, t: list) -> int:
    print(w, n)
    if w == 0 or n == 0:
        return 0

    if t[n][w] != -1:
        return t[n][w]

    if weight[n - 1] <= w:
        include = value[n - 1] + knapsack(value, weight, w - weight[n - 1], n - 1, t)
        discard = knapsack(value, weight, w, n - 1, t)
        t[n][w] = max(include, discard)
        return t[n][w]
    elif weight[n - 1] > w:
        discard = knapsack(value, weight, w, n - 1, t)
        t[n][w] = discard
        return t[n][w]


if __name__ == "__main__":
    inputs = (
        # {
        #     'value': [120, 100, 60],
        #     'weight': [30, 20, 10],
        #     'w': 50,
        #     'n': 3,
        #     'output': 220
        # },
        # {
        #     'value': [20, 5, 10, 40, 15, 25],
        #     'weight': [1, 2, 3, 8, 7, 4],
        #     'w': 10,
        #     'n': 6,
        #     'output': 60
        # },
        {
            'value': [24, 18, 18, 10],
            'weight': [24, 10, 10, 7],
            'w': 25,
            'n': 4,
            'output': 36
        },
    )

    for i in inputs:
        table = [[-1] * (i['w'] + 1)] * (i['n'] + 1)
        o = knapsack(i['value'], i['weight'], i['w'], i['n'], table)
        print(f'Expected Output - {i["output"]}\nOriginal Output - {o}', end='\n\n')