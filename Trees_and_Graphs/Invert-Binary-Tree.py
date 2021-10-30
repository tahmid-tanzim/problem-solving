#!/usr/bin/python3
# https://www.algoexpert.io/questions/Invert%20Binary%20Tree
"""
  Write a function that takes in a Binary Tree and inverts it. In other words,
  the function should swap every left node in the tree for its corresponding
  right node.

  Each BinaryTree node has an integer value, a left child node, and a right child node. Children
  nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree =    1
       /     \
      2       3
    /   \   /   \
   4     5 6     7
 /   \
8     9

Sample Output
       1
    /     \
   3       2
 /   \   /   \
7     6 5     4
            /   \
           9     8
"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTree(tree):
    if tree is None:
        return

    temp = tree.left
    tree.left = tree.right
    tree.right = temp

    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


if __name__ == "__main__":
    # TODO
    pass
