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


if __name__ == "__main__":
    last_item = 1
    prev_permutation = [2, 3]
    for i in range(len(prev_permutation) + 1):
        output_temp = prev_permutation.copy()
        output_temp.insert(i, last_item)
        print(f'{i} Prev Permutation - {prev_permutation} | Output - {output_temp}')
