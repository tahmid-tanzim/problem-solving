#!/usr/bin/python3
# https://www.algoexpert.io/questions/Maximum%20Sum%20Submatrix
"""
  You're given a two-dimensional array (a matrix) of potentially unequal height
  and width that's filled with integers. You're also given a positive integer
  size. Write a function that returns the maximum sum that can be
  generated from a submatrix with dimensions size * size.

For example, consider the following matrix:
[
  [2, 4],
  [5, 6],
  [-3, 2],
]

If size = 2, then the 2x2 submatrices to consider are:
[2, 4]
[5, 6]
"""


# O(w * h) time | O(w * h) space
# where w is the width of the matrix and h is the height
def maximumSumSubmatrix(matrix, size):
    return -1


if __name__ == '__main__':
    print(maximumSumSubmatrix([
        [2, 4],
        [5, 6],
        [-3, 2],
    ], 2))
