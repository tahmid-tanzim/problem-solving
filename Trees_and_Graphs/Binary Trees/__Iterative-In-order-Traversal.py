#!/usr/bin/python3
# https://www.algoexpert.io/questions/Iterative%20In-order%20Traversal
"""
  Write a function that takes in a Binary Tree (where nodes have an additional
  pointer to their parent node) and traverses it iteratively using the in-order
  tree-traversal technique; the traversal should specifically <i>not</i> use
  recursion. As the tree is being traversed, a callback function passed in as an
  argument to the main function should be called on each node (i.e., callback(currentNode)).

  Each BinaryTree node has an integer value, a
  parent node, a left child node, and a
  right child node. Children nodes can either be
  BinaryTree nodes themselves or None / null.

Sample Input
tree =    1
       /     \
      2       3
    /       /   \
   4       6     7
     \
      9
callback = someCallback

Sample Output
// The input callback will have been called in the following order:
callback(4)
callback(9)
callback(2)
callback(1)
callback(6)
callback(3)
callback(7)
"""


# O(n) time | O(1) space
# where n is the number of nodes in the Binary Tree
def iterativeInOrderTraversal(tree, callback):
    pass


if __name__ == "__main__":
    pass
