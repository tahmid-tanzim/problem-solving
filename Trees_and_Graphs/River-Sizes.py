#!/usr/bin/python3
# https://www.algoexpert.io/questions/River%20Sizes
"""
  You're given a two-dimensional array (a matrix) of potentially unequal height
  and width containing only 0s and 1s. Each
  0 represents land, and each 1 represents part of a
  river. A river consists of any number of 1s that are either
  horizontally or vertically adjacent (but not diagonally adjacent). The number
  of adjacent 1s forming a river determine its size.

  Note that a river can twist. In other words, it doesn't have to be a straight
  vertical line or a straight horizontal line; it can be L-shaped, for example.

  Write a function that returns an array of the sizes of all rivers represented
  in the input matrix. The sizes don't need to be in any particular order.

Sample Input
matrix = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0],
]

Sample Output
[1, 2, 2, 2, 5]

// The numbers could be ordered differently.

// The rivers can be clearly seen here:
// [
//   [1,  ,  , 1,  ],
//   [1,  , 1,  ,  ],
//   [ ,  , 1,  , 1],
//   [1,  , 1,  , 1],
//   [1,  , 1, 1,  ],
// ]
"""


# Solution BFS
# O(w * h) time, O(w * h) space
def riverSizes(matrix):
    RIVER_SIZES = list()
    row = 0
    while row < len(matrix):
        col = 0
        while col < len(matrix[0]):
            if matrix[row][col] == 0:
                # Mark as Visited
                matrix[row][col] = -1
                print(f'1. Discovered ZERO - ({row},{col})')
            if matrix[row][col] == 1:
                # Traverse as BFS
                queue = [(row, col)]
                currentRiverSize = 0
                while len(queue) > 0:
                    r, c = queue.pop(0)
                    if matrix[r][c] == 0:
                        # Mark as Visited
                        matrix[r][c] = -1
                        print(f'2. Discovered ZERO - ({r},{c})')
                    if matrix[r][c] == 1:
                        currentRiverSize += 1
                        # Mark as Visited
                        matrix[r][c] = -1
                        print(f'3. Discovered ONE - ({r},{c})')
                        # TOP Cell
                        if r - 1 >= 0:
                            queue.append(tuple((r - 1, c)))
                        # RIGHT Cell
                        if c + 1 < len(matrix[0]):
                            queue.append(tuple((r, c + 1)))
                        # BOTTOM Cell
                        if r + 1 < len(matrix):
                            queue.append(tuple((r + 1, c)))
                        # LEFT Cell
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
