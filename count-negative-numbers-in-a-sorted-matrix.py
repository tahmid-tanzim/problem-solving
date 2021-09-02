#!/usr/bin/python3
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/


def count_negatives(grid):
    count = 0
    for row in grid:
        i = len(row) - 1
        while i >= 0:
            if row[i] >= 0:
                break
            count += 1
            i -= 1
    return count


if __name__ == '__main__':
    print(count_negatives([
        [4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3]
    ]))

    print(count_negatives([
        [3, 2],
        [1, 0]
    ]))

    print(count_negatives([
        [1, -1],
        [-1, -1]
    ]))

    print(count_negatives([[-1]]))
