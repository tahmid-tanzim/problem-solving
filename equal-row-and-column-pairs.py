#!/usr/bin/python3
# https://leetcode.com/problems/equal-row-and-column-pairs/
from typing import List


def getColumnArray(grid: List[List[int]], colIdx) -> List[int]:
    array = []
    for row in grid:
        array.append(row[colIdx])
    return array


def equalPairs(grid: List[List[int]]) -> int:
    n = len(grid)
    count = 0
    for c in range(n):
        for r in range(n):
            if grid[r] == getColumnArray(grid, c):
                count += 1
    return count


if __name__ == "__main__":
    print(equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]), 1)
    print(equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]), 3)
