#!/usr/bin/python3
# Cracking the Coding Interview - 8.2
import time


# Dynamic Programming - Robot in a Grid
def getPath(maze: list, row, col, path=[], visitedBlockedCell=[]):
    if row < 0 or col < 0 or not maze[row][col]:
        return False

    if f"{row}-{col}" in visitedBlockedCell:
        return False

    isAtOrigin = row == 0 and col == 0
    isAvailablePreviousRow = getPath(maze, row - 1, col, path, visitedBlockedCell)
    isAvailablePreviousCol = getPath(maze, row, col - 1, path, visitedBlockedCell)
    if isAtOrigin or isAvailablePreviousRow or isAvailablePreviousCol:
        path.append({
            "row": row,
            "col": col
        })
        return True

    visitedBlockedCell.append(f"{row}-{col}")
    return False


if __name__ == "__main__":
    mazeOne = [
        [True, False, False],
        [True, True, False],
        [False, True, True],
        [True, False, True]
    ]

    mazeTwo = [
        [True, False, True],
        [True, False, False],
        [False, True, True],
        [True, False, True]
    ]

    mazeThree = [
        [True, True, True, True, True, True, False, False, False, False],
        [False, False, True, False, False, True, True, True, False, True],
        [True, True, True, False, True, True, True, True, True, False],
        [True, True, True, True, False, False, True, False, True, True],
        [True, True, False, True, True, False, False, True, False, True],
        [False, True, True, False, True, True, True, False, True, True],
        [True, False, True, True, False, False, True, True, True, False],
        [True, True, True, True, True, True, True, False, True, True],
        [False, True, True, False, True, True, False, True, False, True],
        [True, False, True, False, True, True, True, True, True, True]
    ]
    # Result
    # availablePath = [
    #     {"row": 0, "col": 0},
    #     {"row": 0, "col": 1},
    #     {"row": 0, "col": 2},
    #     {"row": 1, "col": 2},
    #     {"row": 2, "col": 2},
    #     {"row": 3, "col": 2},
    #     {"row": 3, "col": 3},
    #     {"row": 4, "col": 3},
    #     {"row": 4, "col": 4},
    #     {"row": 5, "col": 4},
    #     {"row": 5, "col": 5},
    #     {"row": 5, "col": 6},
    #     {"row": 6, "col": 6},
    #     {"row": 6, "col": 7},
    #     {"row": 6, "col": 8},
    #     {"row": 7, "col": 8},
    #     {"row": 7, "col": 9},
    #     {"row": 8, "col": 9},
    #     {"row": 9, "col": 9},
    # ]

    availablePath = list()
    start = time.time()
    isPathAvailable = getPath(mazeThree, len(mazeThree) - 1, len(mazeThree[0]) - 1, availablePath)
    print("Time Taken - {:.2f} millisecond".format((time.time() - start) * 1000))
    if isPathAvailable:
        print(f'Answer - {len(availablePath)}\n{availablePath}')
    else:
        print(f'Sorry path is not available - {availablePath}')
