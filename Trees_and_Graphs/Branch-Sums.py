#!/usr/bin/python3
# https://www.algoexpert.io/questions/Branch%20Sums
"""
TREE
              1
          /       \
        2          3
    /      \     /    \
   4        5   6      7
 /  \     /
8    9  10

OUTPUT = [15, 16, 18, 10, 11]
Descriptions - The sum of all values in binary tree branch from root to leaf node
"""


# O(n) time & O(n) space
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preOrder(root, total, branch_sum):
    if root is None:
        return

    total += root.value

    if root.left is None and root.right is None:
        branch_sum.append(total)
        total = 0

    preOrder(root.left, total, branch_sum)
    preOrder(root.right, total, branch_sum)
    return branch_sum


def branchSums(root):
    return preOrder(root, 0, [])


if __name__ == "__main__":
    # TODO Create Binary Tree and Find Branch Sums
    pass
