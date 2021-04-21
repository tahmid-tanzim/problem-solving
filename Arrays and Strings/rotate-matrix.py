#!/usr/bin/python3
# Cracking the Coding Interview - 1.7

from typing import List


def rotate(matrix: List[List[int]]) -> bool:
    n = len(matrix)
    if n == 0 or n != len(matrix[0]):
        return False

    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        offset = 0
        for i in range(first, last, 1):
            # offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
            offset += 1

    return True


if __name__ == '__main__':
    inputs = [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ],
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
    ]
    results = [
        [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
        ],
        [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4],
        ]
    ]
    for x in inputs:
        m = x.copy()
        output = rotate(m)
        result = results.pop(0)
        if output:
            assert m == result, "Matrix not rotated by 90 degrees."
        print(output)
