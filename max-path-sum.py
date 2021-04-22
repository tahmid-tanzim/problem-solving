#!/usr/bin/python3

def totalPath(node, value=0):
    if node is None:
        return value

    left = totalPath(node.left, value + node.value)
    right = totalPath(node.right, value + node.value)
    return max(left, right)


def maxPathSum(tree):
    result = 0
    totalLeftSum = totalPath(tree.left)
    totalRightSum = totalPath(tree.right)
    if tree.value > 0:
        result += tree.value
    if totalLeftSum > 0:
        result += totalLeftSum
    if totalRightSum > 0:
        result += totalRightSum
    return result


def total(grid):
    result = 0
    for row in grid:
        for val in row:
            result += val
    return result


if __name__ == "__main__":
    grid1 = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    grid2 = [
        [9, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [3, 0, 0, 6, 0, 1, 0, 7, 8],
        [5, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 2, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 8]
    ]
    print(f'G1 {max(grid1, grid2, key=total)}')
