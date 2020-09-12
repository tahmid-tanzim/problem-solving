#!/usr/local/bin/python3
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# https://www.youtube.com/watch?v=fJbIuhs24zQ

"""
# Dynamic Programming
# 0/1 Knapsack
# Memoization
# Top Down
"""

# row ~> n
# col ~> w
memoization_table = list()


# Method 1: Recursion.
def knapsack_recursive(value: list, weight: list, w: int, n: int) -> int:
    """
    Recursive Function
    """
    # Base Condition
    if w == 0 or n == 0:
        return 0

    # Memoization
    if memoization_table[n][w] != -1:
        return memoization_table[n][w]

    # Choice Diagram
    if weight[n - 1] <= w:
        include = value[n - 1] + knapsack_recursive(value, weight, w - weight[n - 1], n - 1)
        exclude = knapsack_recursive(value, weight, w, n - 1)
        memoization_table[n][w] = max(include, exclude)
        return memoization_table[n][w]
    elif weight[n - 1] > w:
        exclude = knapsack_recursive(value, weight, w, n - 1)
        memoization_table[n][w] = exclude
        return memoization_table[n][w]


# Method 2: Top Down.
def knapsack_top_down(value: list, weight: list, w: int, n: int) -> int:
    """
    Top Down
    """
    # Initialize with Base Condition
    # Don't initialize Matrix like this
    # matrix = [[-1] * (w + 1)] * (n + 1)
    matrix = [[-1 for _ in range(w + 1)] for _ in range(n + 1)]
    r = 0
    while r <= n:
        matrix[r][0] = 0
        r += 1
    c = 1
    while c <= w:
        matrix[0][c] = 0
        c += 1

    r = 1
    while r <= n:
        c = 1
        while c <= w:
            if weight[r - 1] <= c:
                include = value[r - 1] + matrix[r - 1][c - weight[r - 1]]
                exclude = matrix[r - 1][c]
                matrix[r][c] = max(include, exclude)
            else:
                exclude = matrix[r - 1][c]
                matrix[r][c] = exclude
            c += 1
        r += 1

    return matrix[n][w]


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
        memoization_table = [[-1 for x in range(i['w'] + 1)] for y in range(i['n'] + 1)]
        # o = knapsack_recursive(i['value'], i['weight'], i['w'], i['n'])
        o = knapsack_top_down(i['value'], i['weight'], i['w'], i['n'])
        print(f'Expected Output - {i["output"]}\nOriginal Output - {o}', end='\n\n')
