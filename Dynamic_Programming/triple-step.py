#!/usr/bin/python3
# Cracking the Coding Interview - 8.1


# Dynamic Programming
# Time complexity - O(3 ^ n)
def tripleStep(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return tripleStep(n - 1) + tripleStep(n - 2) + tripleStep(n - 3)


# Dynamic Programming with Tabulation
# BottomUp Approach
# Time complexity - O(n)
def countWaysTabulation(n):
    table = [None] * (n + 1)
    table[0] = 1
    table[1] = 1
    table[2] = 2
    i = 3
    while i <= n:
        table[i] = table[i - 1] + table[i - 2] + table[i - 3]
        i += 1
    return table[-1]


# Dynamic Programming with Memoization
# TopDown Approach
# Time complexity - O(n)
def countWays(n):
    return tripleStepWithMemoization(n, [None] * (n + 1))


def tripleStepWithMemoization(n, matrix):
    if n < 0:
        return 0
    if n == 0:
        return 1

    if matrix[n] is not None:
        return matrix[n]

    matrix[n] = tripleStepWithMemoization(n - 1, matrix) + tripleStepWithMemoization(n - 2, matrix) + tripleStepWithMemoization(n - 3, matrix)
    return matrix[n]


if __name__ == "__main__":
    # print(f'Answer - {tripleStep(5)}')
    print(f'Answer with Memoization - {countWays(45)}')
    print(f'Answer with Tabulation - {countWaysTabulation(45)}')
