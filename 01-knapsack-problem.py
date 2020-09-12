#!/usr/local/bin/python3
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# https://www.youtube.com/watch?v=fJbIuhs24zQ

"""
# Dynamic Programming
# 0/1 Knapsack
# Memoization
# Top Down
"""


def knapsack_recursive(value: list, weight: list, w: int, n: int, table: list) -> int:
    """
    Recursive Function
    """
    print(w, n)
    # Base Condition
    if w == 0 or n == 0:
        return 0

    # Memoization
    if table[n][w] != -1:
        return table[n][w]

    # Choice Diagram
    if weight[n - 1] <= w:
        include = value[n - 1] + knapsack_recursive(value, weight, w - weight[n - 1], n - 1, table)
        discard = knapsack_recursive(value, weight, w, n - 1, table)
        table[n][w] = max(include, discard)
        return table[n][w]
    elif weight[n - 1] > w:
        discard = knapsack_recursive(value, weight, w, n - 1, table)
        table[n][w] = discard
        return table[n][w]


def knapsack_top_down(value: list, weight: list, w: int, n: int) -> int:
    """
    Top Down
    """
    # Initialize with Base Condition
    # table = [[-1] * (w + 1)] * (n + 1)
    table = [[-1 for _ in range(w + 1)] for _ in range(n + 1)]
    r = 0
    while r <= n:
        table[r][0] = 0
        r += 1
    c = 1
    while c <= w:
        table[0][c] = 0
        c += 1

    r = 1
    while r <= n:
        c = 1
        while c <= w:
            if weight[r - 1] <= c:
                include = value[r - 1] + table[r - 1][c - weight[r - 1]]
                discard = table[r - 1][c]
                table[r][c] = max(include, discard)
            else:
                discard = table[r - 1][c]
                table[r][c] = discard
            c += 1
        r += 1

    return table[n][w]


if __name__ == "__main__":
    inputs = (
        {
            'value': [120, 100, 60],
            'weight': [30, 20, 10],
            'w': 50,
            'n': 3,
            'output': 220
        },
        {
            'value': [20, 5, 10, 40, 15, 25],
            'weight': [1, 2, 3, 8, 7, 4],
            'w': 10,
            'n': 6,
            'output': 60
        },
        {
            'value': [24, 18, 18, 10],
            'weight': [24, 10, 10, 7],
            'w': 25,
            'n': 4,
            'output': 36
        },
    )

    for i in inputs:
        # t = [[-1] * (i['w'] + 1)] * (i['n'] + 1)
        # t = [[-1 for x in range(i['w'] + 1)] for y in range(i['n'] + 1)]
        # o = knapsack_recursive(i['value'], i['weight'], i['w'], i['n'], t)
        o = knapsack_top_down(i['value'], i['weight'], i['w'], i['n'])
        print(f'Expected Output - {i["output"]}\nOriginal Output - {o}', end='\n\n')
