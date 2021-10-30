#!/usr/bin/python3
# https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Traverse%20Graph
"""
  You're given two positive integers representing the width and height of a
  grid-shaped, rectangular graph. Write a function that returns the number of
  ways to reach the bottom right corner of the graph when starting at the top
  left corner. Each move you take must either go down or right. In other words,
  you can never move up or left in the graph.

  For example, given the graph illustrated below, with width = 2 and height = 3, there are three ways to
  reach the bottom right corner when starting at the top left corner:
     _ _
    |_|_|
    |_|_|
    |_|_|

  - Down, Down, Right
  - Right, Down, Down
  - Down, Right, Down

  Note: you may assume that `width * height >= 2`. In other words, the graph will never be a 1x1 grid.
"""


# O(n+m) time, O(1) space
# n is width and m is height of the graph
def numberOfWaysToTraverseGraphIteration(width, height):
    # Initialize Grid
    # Height == Row
    # Width == Column
    numberOfWays = []
    for r in range(height):
        row = []
        for c in range(width):
            if r == 0 or c == 0:
                row.append(1)
            else:
                row.append(0)
        numberOfWays.append(row)

    for r in range(1, height):
        for c in range(1, width):
            numberOfWays[r][c] = numberOfWays[r - 1][c] + numberOfWays[r][c - 1]

    return numberOfWays[height - 1][width - 1]


def findWaysToTraverse(w, h, matrix):
    if matrix[h][w] is not None:
        return matrix[h][w]

    if w == 0 or h == 0:
        matrix[h][w] = 1
        return 1

    matrix[h][w] = findWaysToTraverse(w - 1, h, matrix) + findWaysToTraverse(w, h - 1, matrix)
    return matrix[h][w]


def numberOfWaysToTraverseGraphRecursion(width, height):
    memoization_matrix = [[None for c in range(width)] for r in range(height)]
    return findWaysToTraverse(width - 1, height - 1, memoization_matrix)


if __name__ == '__main__':
    # Output ~> 10
    print(numberOfWaysToTraverseGraphIteration(width=4, height=3))
    print(numberOfWaysToTraverseGraphRecursion(width=4, height=3))
