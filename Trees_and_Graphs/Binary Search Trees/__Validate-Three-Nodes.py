#!/usr/bin/python3
# https://www.algoexpert.io/questions/Validate%20Three%20Nodes
"""
  You're given three nodes that are contained in the same Binary Search Tree:
  nodeOne, nodeTwo, and nodeThree. Write
  a function that returns a boolean representing whether one of
  nodeOne or nodeThree is an ancestor of
  nodeTwo and the other node is a descendant of
  nodeTwo. For example, if your function determines that
  nodeOne is an ancestor of nodeTwo, then it needs to
  see if nodeThree is a descendant of nodeTwo. If your
  function determines that nodeThree is an ancestor, then it needs
  to see if nodeOne is a descendant.

  A descendant of a node N is defined as a node contained in
  the tree rooted at N. A node N is an ancestor of
  another node M if M is a descendant of N.

  It isn't guaranteed that nodeOne or nodeThree will
  be ancestors or descendants of nodeTwo, but it is guaranteed that
  all three nodes will be unique and will never be None /
  null. In other words, you'll be given valid input nodes.

  Each BST node has an integer value, a
  left child node, and a right child node. A node is
  said to be a valid BST node if and only if it satisfies the BST
  property: its value is strictly greater than the values of every
  node to its left; its value is less than or equal to the values
  of every node to its right; and its children nodes are either valid
  BST nodes themselves or None / null.

Sample Input
tree =    5
       /     \
      2       7
    /   \   /   \
   1     4 6     8
  /     /
 0     3  
// This tree won't actually be passed as an input; it's here to help you visualize the problem.
nodeOne = 5 // The actual node with value 5.
nodeTwo = 2 // The actual node with value 2.
nodeThree = 3 // The actual node with value 3.

Sample Output
true // nodeOne is an ancestor of nodeTwo, and nodeThree is a descendant of nodeTwo.
"""


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(d) time | O(1) space
# where d is the distance between nodeOne and nodeThree
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    return False


if __name__ == "__main__":
    # TODO
    pass
