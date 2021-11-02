#!/usr/bin/python3
# https://www.algoexpert.io/questions/Compare%20Leaf%20Traversal
"""
  Write a function that takes in the root nodes of two Binary Trees and returns
  a boolean representing whether their leaf traversals are the same.

  The leaf traversal of a Binary Tree traverses only its leaf nodes from left to
  right. A leaf node is any node that has no left or right children.

  For example, the leaf traversal of the following Binary Tree is 1, 3, 2.

   4
 /   \
1     5
    /   \
   3     2

  Each BinaryTree node has an integer value, a
  left child node, and a right child node. Children
  nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree1 = 1
      /   \
     2     3
   /   \     \
  4     5     6
      /   \
     7     8
tree2 = 1
      /   \
     2     3
   /   \    \
  4     7    5
            /  \
           8    6

Sample Output
true
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n + m) time, O(h1 + h2) space
# where n is the number of nodes in the first Binary Tree,
# m is the number in the second, h1 is the height of the first Binary Tree
# and h2 is the height of the second.
class Solution1:
    @staticmethod
    def getNextLeaf(stack):
        while len(stack) != 0:
            node = stack.pop()
            if node.left is None and node.right is None:
                return node.value
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return None

    def compareLeafTraversal(self, tree1, tree2):
        stack1 = [tree1]
        stack2 = [tree2]

        while len(stack1) > 0 and len(stack2) > 0:
            leaf1 = self.getNextLeaf(stack1)
            leaf2 = self.getNextLeaf(stack2)

            if leaf1 is None or leaf2 is None:
                break
            elif leaf1 != leaf2:
                return False

        return len(stack1) == len(stack2)


class Solution2:
    def preorder(self, node, leaf):
        if node is None:
            return

        if node.left is None and node.right is None:
            leaf.append(node.value)
            return

        self.preorder(node.left, leaf)
        self.preorder(node.right, leaf)

    def compareLeafTraversal(self, tree1, tree2):
        leaf1 = list()
        self.preorder(tree1, leaf1)

        leaf2 = list()
        self.preorder(tree2, leaf2)

        return leaf1 == leaf2


if __name__ == "__main__":
    # TODO
    pass
