#!/usr/bin/python3
# https://www.algoexpert.io/questions/Solve%20Sudoku


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
