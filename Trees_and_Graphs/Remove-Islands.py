#!/usr/bin/python3
# https://www.algoexpert.io/questions/Remove%20Islands
"""
You're given a two-dimensional array (a matrix) of potentially unequal height
and width containing only 0s and 1s. The matrix
represents a two-toned image, where each 1 represents black and
each 0 represents white. An island is defined as any number of
1s that are horizontally or vertically adjacent (but not
diagonally adjacent) and that don't touch the border of the image. In other
words, a group of horizontally or vertically adjacent 1s isn't an
island if any of those 1s are in the first row, last row, first
column, or last column of the input matrix.

Note that an island can twist. In other words, it doesn't have to be a
straight vertical line or a straight horizontal line; it can be L-shaped, for
example.

You can think of islands as patches of black that don't touch the border of
the two-toned image.

Write a function that returns a modified version of the input matrix, where
all of the islands are removed. You remove an island by replacing it with
0s.

Naturally, you're allowed to mutate the input matrix.
"""


def breadthFirstSearch(matrix, r, c, m, n):
    queue = [(r, c)]
    while len(queue) > 0:
        row, col = queue.pop(0)
        if matrix[row][col] == 1:
            matrix[row][col] += 1
        # TOP
        if row - 1 >= 0 and matrix[row - 1][col] == 1:
            queue.append((row - 1, col))
        # RIGHT
        if col + 1 < n and matrix[row][col + 1] == 1:
            queue.append((row, col + 1))
        # BOTTOM
        if row + 1 < m and matrix[row + 1][col] == 1:
            queue.append((row + 1, col))
        # LEFT
        if col - 1 >= 0 and matrix[row][col - 1] == 1:
            queue.append((row, col - 1))


# O(w * h) time, O(w * h) space
def removeIslands(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for r in (0, m - 1):
        for c in range(0, n):
            if matrix[r][c] == 1:
                breadthFirstSearch(matrix, r, c, m, n)

    for c in (0, n - 1):
        for r in range(0, m):
            if matrix[r][c] == 1:
                breadthFirstSearch(matrix, r, c, m, n)

    for r in range(m):
        for c in range(n):
            if matrix[r][c] > 0:
                matrix[r][c] -= 1

    return matrix


if __name__ == "__main__":
    OUTPUT = removeIslands([
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ])
    print(OUTPUT)

    # Output
    # [
    #     [1, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 1, 1, 1],
    #     [0, 0, 0, 0, 1, 0],
    #     [1, 1, 0, 0, 1, 0],
    #     [1, 0, 0, 0, 0, 0],
    #     [1, 0, 0, 0, 0, 1],
    # ]
