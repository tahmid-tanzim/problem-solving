#!/usr/bin/python3
# https://www.youtube.com/playlist?list=PL_z_8CaSLPWfxJPz2-YKqL9gXWdgrhvdn
# https://leetcode.com/problems/diameter-of-binary-tree/
# https://www.algoexpert.io/questions/Binary%20Tree%20Diameter
# Dynamic Programming on Tree
# DP on Tree
# maximum number of nodes between 2 leaf nodes
from TreeNode import create_binary_tree


def heightOfBinaryTree(node) -> int:
    if node is None:
        return 0
    leftHeight = heightOfBinaryTree(node.left)
    rightHeight = heightOfBinaryTree(node.right)
    actualHeight = 1 + max(leftHeight, rightHeight)
    return actualHeight


def diameterOfBinaryTree(root) -> int:
    if root is None:
        return 0

    leftHeight = heightOfBinaryTree(root.left)
    rightHeight = heightOfBinaryTree(root.right)
    leftDiameter = diameterOfBinaryTree(root.left)
    rightDiameter = diameterOfBinaryTree(root.right)

    # Longest diameter formed either in left or right child. diameter path doesn't passed through root node
    diameterFromChild = max(leftDiameter, rightDiameter)

    # Forming diameter starting from `left` leaf child to `right` leaf child through root node
    diameterIncludingRoot = 1 + leftHeight + rightHeight

    return max(diameterFromChild, diameterIncludingRoot)


if __name__ == "__main__":
    tree_array = [1, 2, 3, 4, 5]
    root_node = create_binary_tree(tree_array)
    print(diameterOfBinaryTree(root_node))
