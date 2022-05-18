import sys
# import math

w, h = [int(i) for i in input().split()]
diagram = []
# print(f"({w},{h})", file=sys.stderr, flush=True)

for i in range(h):
    line = input()
    diagram.append(" " + line + " ")

for startingCollumnIdx in range(1, w + 1, 3):
    # print(diagram[0][colIdx], diagram[h-1][colIdx], file=sys.stderr, flush=True)
    TB = diagram[0][startingCollumnIdx]
    rowIdx = 1
    currentCollumnIdx = startingCollumnIdx
    while rowIdx < h:
        # Check Left
        if diagram[rowIdx][currentCollumnIdx - 1] == '-':
            currentCollumnIdx -= 3
        # Check Right
        elif diagram[rowIdx][currentCollumnIdx + 1] == '-':
            currentCollumnIdx += 3
        rowIdx += 1
    TB += diagram[rowIdx - 1][currentCollumnIdx]
    print(TB)
