#!/usr/bin/python3
# https://www.algoexpert.io/questions/Node%20Depths
"""
TREE
              1
          /       \
        2          3
    /      \     /    \
   4        5   6      7
 /  \
8    9

OUTPUT = 16
Descriptions - Distance between a node in a Binary Tree and the tree's root is called the node's depth.
Write a function that takes in a Binary Tree and returns the sum of its nodes' depth.
"""


# O(n) time & O(h) space
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preOrder(root, level):
    if root is None:
        return 0
    return level + preOrder(root.left, level + 1) + preOrder(root.right, level + 1)


def nodeDepths1(root):
    return preOrder(root, 0)


# BFS Iterative
def nodeDepths2(root):
    queue = [(root, 0)]
    total = 0
    while len(queue) > 0:
        current_node, depth = queue.pop(0)
        if current_node is not None:
            total += depth
            queue.append((current_node.left, depth + 1))
            queue.append((current_node.right, depth + 1))
    return total


if __name__ == "__main__":
    # TODO Create Binary Tree and Find Node Depths
    pass
