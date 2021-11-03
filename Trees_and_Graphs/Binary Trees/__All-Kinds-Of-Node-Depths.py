#!/usr/bin/python3
# https://www.algoexpert.io/questions/All%20Kinds%20Of%20Node%20Depths
"""
  The distance between a node in a Binary Tree and the tree's root is called the node's depth.

  Write a function that takes in a Binary Tree and returns the sum of all of its subtrees' nodes' depths.

  Each BinaryTree node has an integer value, a
  left child node, and a right child node. Children
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
26
// The sum of the root tree's node depths is 16.
// The sum of the tree rooted at 2's node depths is 6.
// The sum of the tree rooted at 3's node depths is 2.
// The sum of the tree rooted at 4's node depths is 2.
// Summing all of these sums yields 26.
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Average case: when the tree is balanced
# O(n) time | O(h) space - where n is the number of nodes in the Binary Tree and h is the height of the Binary Tree
def allKindsOfNodeDepths(root):
    pass


if __name__ == "__main__":
    pass
