#!/usr/bin/python3
# https://www.algoexpert.io/questions/Zigzag%20Traverse
"""
  Write a function that takes in an n x m two-dimensional array (that can be
  square-shaped when n == m) and returns a one-dimensional array of all the
  array's elements in zigzag order.

  Zigzag order starts at the top left corner of the two-dimensional array, goes
  down by one element, and proceeds in a zigzag pattern all the way to the
  bottom right corner.

Sample Input
array = [
  [1,  3,  4, 10],
  [2,  5,  9, 11],
  [6,  8, 12, 15],
  [7, 13, 14, 16],
]

Sample Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""


# O(n) time | O(n) space - where n is the total number of elements in the two-dimensional array
def zigzagTraverse(array):
    row_size = len(array)
    if row_size == 1:
        return array[0]

    col_size = len(array[0])
    zigzag_array = list()
    if col_size == 1:
        for row in array:
            zigzag_array = zigzag_array + row
        return zigzag_array

    direction = 'DOWN-LEFT'
    row = 0
    col = 0

    for i in range(row_size * col_size):
        print(f'{i} - {array[row][col]}')
        zigzag_array.append(array[row][col])

        if direction == 'DOWN-LEFT':
            if row == row_size - 1:
                direction = 'RIGHT'
                col += 1
            elif col == 0:
                direction = 'DOWN'
                row += 1
            else:
                row += 1
                col -= 1
            continue

        if direction == 'UP-RIGHT':
            if col == col_size - 1:
                direction = 'DOWN'
                row += 1
            elif row == 0:
                direction = 'RIGHT'
                col += 1
            else:
                row -= 1
                col += 1
            continue

        if direction == 'DOWN':
            if col == 0:
                direction = 'UP-RIGHT'
                row -= 1
                col += 1
            elif col == col_size - 1:
                direction = 'DOWN-LEFT'
                row += 1
                col -= 1
            continue

        if direction == 'RIGHT':
            if row == 0:
                direction = 'DOWN-LEFT'
                row += 1
                col -= 1
            elif row == row_size - 1:
                direction = 'UP-RIGHT'
                row -= 1
                col += 1
            continue

    return zigzag_array


if __name__ == '__main__':
    # arr = [
    #     [1, 3],
    #     [2, 4],
    #     [5, 7],
    #     [6, 8],
    #     [9, 10]
    # ]

    arr = [
        [1, 3, 4, 10],
        [2, 5, 9, 11],
        [6, 8, 12, 15],
        [7, 13, 14, 16],
    ]
    print(f'Answer - {zigzagTraverse(arr)}')
