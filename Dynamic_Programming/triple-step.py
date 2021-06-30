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


# Dynamic Programming with Memoization
# Time complexity - O(n)
def countWays(n):
    return tripleStepWithMemoization(n, [None] * (n + 1))


def tripleStepWithMemoization(n, matrix):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif matrix[n] is not None:
        return matrix[n]

    matrix[n] = tripleStep(n - 1) + tripleStep(n - 2) + tripleStep(n - 3)
    return matrix[n]


if __name__ == "__main__":
    print(f'Answer - {tripleStep(5)}')
    print(f'Answer with Memoization - {countWays(5)}')
