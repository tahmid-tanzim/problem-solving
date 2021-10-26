#!/usr/bin/python3
# https://www.youtube.com/playlist?list=PL_z_8CaSLPWfxJPz2-YKqL9gXWdgrhvdn
# https://www.algoexpert.io/questions/Binary%20Tree%20Diameter
# Dynamic Programming on Tree
# DP on Tree
from TreeNode import create_binary_tree


def height(node):
    if node is None:
        return 0

    leftH = height(node.left)
    rightH = height(node.right)
    return 1 + max(leftH, rightH)


def diameter(node, value):
    if node is None:
        return

    leftHeight = height(node.left)
    rightHeight = height(node.right)
    value = max(value, leftHeight + rightHeight)
    diameter(node.left, value)
    diameter(node.right, value)
    print(value)
    return value


def binaryTreeDiameter(tree):
    return diameter(tree, 0)


if __name__ == "__main__":
    tree_array = [1, 2, 3, 4, 5]
    root_node = create_binary_tree(tree_array)
    obj = Solution()
    print(obj.diameterOfBinaryTree(root_node))
