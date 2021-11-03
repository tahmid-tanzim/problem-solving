#!/usr/bin/python3
# https://www.algoexpert.io/questions/Flatten%20Binary%20Tree
"""
  Write a function that takes in a Binary Tree, flattens it, and returns its leftmost node.

  A flattened Binary Tree is a structure that's nearly identical to a Doubly
  Linked List (except that nodes have left and
  right pointers instead of prev and
  next pointers), where nodes follow the original tree's left-to-right order.

  Note that if the input Binary Tree happens to be a valid Binary Search Tree,
  the nodes in the flattened tree will be sorted.

  The flattening should be done in place, meaning that the original data
  structure should be mutated (no new structure should be created).

  Each BinaryTree node has an integer value, a
  left child node, and a right child node. Children
  nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree =      1
         /     \
        2       3
      /   \   /
     4     5 6
          / \
         7   8

Sample Output
4 <-> 2 <-> 7 <-> 5 <-> 8 <-> 1 <-> 6 <-> 3 // the leftmost node with value 4
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(d) space
# where n is the number of nodes in the Binary Tree and d is the depth (height) of the Binary Tree
def flattenBinaryTree(root):
    pass


if __name__ == "__main__":
    pass
