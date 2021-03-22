#!/usr/bin/python3
"""
@Topic Graph, BFS, Breadth First Search
@URL https://www.algoexpert.io/questions/River%20Sizes
"""


def riverSizes(matrix):
    RIVER_SIZES = list()
    row = 0
    while row < len(matrix):
        col = 0
        while col < len(matrix[0]):
            # if matrix[row][col] == 0:
            #     # Mark as Visited
            #     matrix[row][col] = -1
            #     print(f'0. Discovered - ({r},{c})')
            if matrix[row][col] == 1:
                queue = [(row, col)]
                currentRiverSize = 0
                while len(queue) > 0:
                    r, c = queue.pop(0)
                    if matrix[r][c] == 0:
                        # Mark as Visited
                        matrix[r][c] = -1
                        print(f'0. Discovered - ({r},{c})')
                    if matrix[r][c] == 1:
                        currentRiverSize += 1
                        # Mark as Visited
                        matrix[r][c] = -1
                        print(f'1. Discovered - ({r},{c})')
                        # TOP
                        if r - 1 >= 0:
                            queue.append(tuple((r - 1, c)))
                        # RIGHT
                        if c + 1 < len(matrix[0]):
                            queue.append(tuple((r, c + 1)))
                        # BOTTOM
                        if r + 1 < len(matrix):
                            queue.append(tuple((r + 1, c)))
                        # LEFT
                        if c - 1 >= 0:
                            queue.append(tuple((r, c - 1)))
                RIVER_SIZES.append(currentRiverSize)
            col += 1
        row += 1
    return RIVER_SIZES


if __name__ == "__main__":
    OUTPUT = riverSizes([
        [1, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 0, 0],
    ])
    print(OUTPUT)
    # OUTPUT = [2, 1, 6, 1, 5]
