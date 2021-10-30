#!/usr/bin/python3
# https://www.algoexpert.io/questions/Binary%20Tree%20Diameter
"""
  Write a function that takes in a Binary Tree and returns its diameter. The
  diameter of a binary tree is defined as the length of its longest path, even
  if that path doesn't pass through the root of the tree.

  A path is a collection of connected nodes in a tree, where no node is
  connected to more than two other nodes. The length of a path is the number of
  edges between the path's first node and its last node.

  Each BinaryTree node has an integer value, a
  left child node, and a right child node. Children
  nodes can either be BinaryTree nodes themselves or
  None / null.

Sample Input
tree =        1
            /   \
           3     2
         /   \ 
        7     4
       /       \
      8         5
     /           \
    9             6

Sample Output
6 
// 9 ~> 8 ~> 7 ~> 3 ~> 4 ~> 5 ~> 6
// There are 6 edges between the
// first node and the last node
// of this tree's longest path.
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


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
    # TODO
    pass
