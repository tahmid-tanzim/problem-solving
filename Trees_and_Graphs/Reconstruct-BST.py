#!/usr/bin/python3
# https://www.algoexpert.io/questions/Reconstruct%20BST
"""
  The pre-order traversal of a Binary Tree is a traversal technique that starts
  at the tree's root node and visits nodes in the following order:

  - Current node
  - Left subtree
  - Right subtree

  Given a non-empty array of integers representing the pre-order traversal of a
  Binary Search Tree (BST), write a function that creates the relevant BST and
  returns its root node.

  The input array will contain the values of BST nodes in the order in which
  these nodes would be visited with a pre-order traversal.

  Each BST node has an integer value, a
  left child node, and a right child node. A node is
  said to be a valid BST node if and only if it satisfies the BST
  property: its value is strictly greater than the values of every
  node to its left; its value is less than or equal to the values
  of every node to its right; and its children nodes are either valid
  BST nodes themselves or None / null.

Sample Input
preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]

Sample Output
        10
      /    \
     4      17
   /   \      \
  2     5     19
 /           /
1           18
"""


# O(n) time, O(n) space
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Base Case
    if len(preOrderTraversalValues) == 0:
        return

    currentValue = preOrderTraversalValues[0]
    # Assuming no right subtree
    rightSubtreeRootIdx = len(preOrderTraversalValues)
    for idx, value in enumerate(preOrderTraversalValues):
        if value >= currentValue and idx != 0:
            rightSubtreeRootIdx = idx
            break

    leftSubtree = reconstructBst(preOrderTraversalValues[1:rightSubtreeRootIdx])
    rightSubtree = reconstructBst(preOrderTraversalValues[rightSubtreeRootIdx:])
    return BST(currentValue, leftSubtree, rightSubtree)


if __name__ == "__main__":
    print(reconstructBst([10, 4, 2, 1, 5, 17, 19, 18]))
