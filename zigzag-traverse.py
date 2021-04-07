#!/usr/bin/python3
"""
https://www.algoexpert.io/questions/Zigzag%20Traverse
"""


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
    arr = [
        [1, 3],
        [2, 4],
        [5, 7],
        [6, 8],
        [9, 10]
    ]
    print(f'Answer - {zigzagTraverse(arr)}')
