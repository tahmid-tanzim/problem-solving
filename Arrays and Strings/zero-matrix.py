#!/usr/bin/python3
# Cracking the Coding Interview - 1.8

from typing import List


def assignZeroInRow(matrix: List[List[int]], row_index, col_size):
    for j in range(col_size):
        matrix[row_index][j] = 0


def assignZeroInColumn(matrix: List[List[int]], col_index, row_size):
    for i in range(row_size):
        matrix[i][col_index] = 0


def setZeros(matrix: List[List[int]]):
    row_size = len(matrix)
    row = [False] * row_size
    col_size = len(matrix[0])
    column = [False] * col_size

    for i in range(row_size):
        for j in range(col_size):
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True

    for i in range(row_size):
        if row[i]:
            assignZeroInRow(matrix, i, col_size)

    for j in range(col_size):
        if column[j]:
            assignZeroInColumn(matrix, j, row_size)


if __name__ == '__main__':
    inputs = [
        [
            [1, 2, 3],
            [0, 5, 6],
            [7, 8, -1],
        ],
        [
            [1, 2, 3, 4, 100],
            [5, 0, 7, 8, 200],
            [9, 10, -1, 12, 300],
            [13, 14, 15, 0, 400],
        ],
        [
            [1, 2, 3, 0],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [0, 14, 15, 16],
        ]
    ]
    results = [
        [
            [0, 2, 3],
            [0, 0, 0],
            [0, 8, -1],
        ],
        [
            [1, 0, 3, 0, 100],
            [0, 0, 0, 0, 0],
            [9, 0, -1, 0, 300],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0],
            [0, 6, 7, 0],
            [0, 10, 11, 0],
            [0, 0, 0, 0],
        ]
    ]
    for x in inputs:
        m = x.copy()
        setZeros(m)
        result = results.pop(0)
        assert m == result, f"Matrix is NOT valid - {m}"
        print('---------------------------\n', m, '\n', result, end='\n---------------------------')
