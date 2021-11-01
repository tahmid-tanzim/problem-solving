#!/usr/bin/python3
# https://www.algoexpert.io/questions/Solve%20Sudoku
"""
  You're given a two-dimensional array that represents a 9x9 partially filled
  Sudoku board. Write a function that returns the solved Sudoku board.

  Sudoku is a famous number-placement puzzle in which you need to fill a 9x9
  grid with integers in the range of 1-9. Each 9x9 Sudoku board is
  split into 9 3x3 subgrids, as seen in the illustration below, and starts out
  partially filled.

- - 3 | - 2 - | 6 - - 
9 - - | 3 - 5 | - - 1 
- - 1 | 8 - 6 | 4 - -
- - - - - - - - - - - 
- - 8 | 1 - 2 | 9 - -
7 - - | - - - | - - 8 
- - 6 | 7 - 8 | 2 - -
- - - - - - - - - - -
- - 2 | 6 - 9 | 5 - - 
8 - - | 2 - 3 | - - 9
- - 5 | - 1 - | 3 - -

  The objective is to fill the grid such that each row, column, and 3x3 subgrid
  contains the numbers 1-9 exactly once. In other words, no row may
  contain the same digit more than once, no column may contain the same digit
  more than once, and none of the 9 3x3 subgrids may contain the same digit more
  than once.

  Your input for this problem will always be a partially filled 9x9
  two-dimensional array that represents a solvable Sudoku puzzle. Every element
  in the array will be an integer in the range of 0-9, where a
  0 represents an empty square that must be filled by your
  algorithm.

  Note that you may modify the input array and that there will always be exactly
  one solution to each input Sudoku board.

Sample Input
board = 
[
  [7, 8, 0, 4, 0, 0, 1, 2, 0],
  [6, 0, 0, 0, 7, 5, 0, 0, 9],
  [0, 0, 0, 6, 0, 1, 0, 7, 8],
  [0, 0, 7, 0, 4, 0, 2, 6, 0],
  [0, 0, 1, 0, 5, 0, 9, 3, 0],
  [9, 0, 4, 0, 6, 0, 0, 0, 5],
  [0, 7, 0, 3, 0, 0, 0, 1, 2],
  [1, 2, 0, 0, 0, 7, 4, 0, 0],
  [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

Sample Output
[
  [7, 8, 5, 4, 3, 9, 1, 2, 6],
  [6, 1, 2, 8, 7, 5, 3, 4, 9],
  [4, 9, 3, 6, 2, 1, 5, 7, 8],
  [8, 5, 7, 9, 4, 3, 2, 6, 1],
  [2, 6, 1, 7, 5, 8, 9, 3, 4],
  [9, 3, 4, 1, 6, 2, 7, 8, 5],
  [5, 7, 8, 3, 9, 4, 6, 1, 2],
  [1, 2, 6, 5, 8, 7, 4, 9, 3],
  [3, 4, 9, 2, 1, 6, 8, 5, 7],
]
"""


def getEmptyCell(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None


def isValidSudoku(board, i, j, value):
    # Check Valid Row
    for c in range(9):
        if c != j and board[i][c] == value:
            print('Row Invalid')
            return False

    # Check Valid Column
    for r in range(9):
        if r != i and board[r][j] == value:
            print('Col Invalid')
            return False

    row = (i // 3) * 3
    col = (j // 3) * 3
    # Check Valid Subgrid
    for r in range(row, row + 3):
        for c in range(col, col + 3):
            if r != i and c != j and board[r][c] == value:
                print('Subgrid Invalid')
                return False

    return True


def solve(board):
    index = getEmptyCell(board)
    if index is None:
        return True

    r, c = index
    for val in range(1, 10):
        if isValidSudoku(board, r, c, val):
            board[r][c] = val
            if solve(board):
                return True
            board[r][c] = 0

    return False


def solveSudoku(board):
    solve(board)
    return board


if __name__ == '__main__':
    solved_board = solveSudoku([
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ])

    for board_row in solved_board:
        print(board_row)

    # print(solveSudoku([
    #     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    # ]))
