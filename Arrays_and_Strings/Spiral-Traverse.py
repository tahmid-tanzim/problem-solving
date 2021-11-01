#!/usr/bin/python3
# https://www.algoexpert.io/questions/Spiral%20Traverse
"""
  Write a function that takes in an n x m two-dimensional array (that can be
  square-shaped when n == m) and returns a one-dimensional array of all the
  array's elements in spiral order.

  Spiral order starts at the top left corner of the two-dimensional array, goes
  to the right, and proceeds in a spiral pattern all the way until every element
  has been visited.

Sample Input
array = [
  [1,   2,  3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10,  9,  8, 7],
]

Sample Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""


# O(n) time, O(n) space
def spiralTraverse(array):
    output = []
    row_start = 0
    row_end = len(array) - 1
    col_start = 0
    col_end = len(array[0]) - 1

    while row_start <= row_end and col_start <= col_end:
        # ROW Forward
        c = col_start
        while c <= col_end:
            output.append(array[row_start][c])
            c += 1
        row_start += 1

        # COLUMN Downward
        r = row_start
        while r <= row_end:
            output.append(array[r][col_end])
            r += 1
        col_end -= 1

        # ROW Backward
        if row_start <= row_end:
            c = col_end
            while c >= col_start:
                output.append(array[row_end][c])
                c -= 1
            row_end -= 1

        # COLUMN Upward
        if col_start <= col_end:
            r = row_end
            while r >= row_start:
                output.append(array[r][col_start])
                r -= 1
            col_start += 1

    return output


if __name__ == '__main__':
    print(spiralTraverse([
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ]))
