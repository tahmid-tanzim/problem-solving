#!/usr/bin/python3
# https://www.algoexpert.io/questions/Find%20Nodes%20Distance%20K
"""
  You're given the root node of a Binary Tree, a target value of a
  node that's contained in the tree, and a positive integer k.
  Write a function that returns the values of all the nodes that are exactly
  distance k from the node with target value.

  The distance between two nodes is defined as the number of edges that must be
  traversed to go from one node to the other. For example, the distance between
  a node and its immediate left or right child is 1. The same holds
  in reverse: the distance between a node and its parent is 1. In a
  tree of three nodes where the root node has a left and right child, the left
  and right children are distance 2 from each other.

  Each BinaryTree node has an integer value, a
  left child node, and a right child node. Children
  nodes can either be BinaryTree nodes themselves or None / null.

  Note that all BinaryTree node values will be unique, and your
  function can return the output values in any order.

Sample Input
tree = 1
     /   \
    2     3
  /   \     \
 4     5     6
           /   \
          7     8
target = 3
k = 2

Sample Output
[2, 7, 8] // These values could be ordered differently.
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
def findNodesDistanceK(tree, target, k):
    return []


if __name__ == "__main__":
    pass
