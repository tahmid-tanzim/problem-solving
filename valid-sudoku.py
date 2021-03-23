#!/usr/bin/python3
# https://leetcode.com/problems/valid-sudoku/
from typing import List
"""
0 ~ 00 
1 ~ 01
2 ~ 02
3 ~ 10
4 ~ 11
5 ~ 12
6 ~ 20
7 ~ 21
8 ~ 22
"""


def isValidSudoku(board: List[List[str]]) -> bool:
    row = [[] for _ in range(9)]
    col = [[] for _ in range(9)]
    box = [[] for _ in range(9)]
    for r in range(9):
        for c in range(9):
            if board[r][c] != '.':
                val = board[r][c]
                if val in row[r] or val in col[c] or val in box[3 * (r//3) + c//3]:
                    return False
                row[r].append(val)
                col[c].append(val)
                box[3 * (r // 3) + c // 3].append(val)
    return True


if __name__ == '__main__':
    # print(isValidSudoku([
    #     [7, 8, 0, 4, 0, 0, 1, 2, 0],
    #     [6, 0, 0, 0, 7, 5, 0, 0, 9],
    #     [0, 0, 0, 6, 0, 1, 0, 7, 8],
    #     [0, 0, 7, 0, 4, 0, 2, 6, 0],
    #     [0, 0, 1, 0, 5, 0, 9, 3, 0],
    #     [9, 0, 4, 0, 6, 0, 0, 0, 5],
    #     [0, 7, 0, 3, 0, 0, 0, 1, 2],
    #     [1, 2, 0, 0, 0, 7, 4, 0, 0],
    #     [0, 4, 9, 2, 0, 6, 0, 0, 7]
    # ]))
    print(isValidSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))
