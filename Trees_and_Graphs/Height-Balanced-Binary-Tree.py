#!/usr/bin/python3
# https://www.algoexpert.io/questions/Height%20Balanced%20Binary%20Tree
"""
  You're given the root node of a Binary Tree. Write a function that returns
  true if this Binary Tree is height balanced and false if it isn't.

  A Binary Tree is height balanced if for each node in the tree, the difference
  between the height of its left subtree and the height of its right subtree is at most 1.

  Each BinaryTree node has an integer value, a
  left child node, and a right child node. Children
  nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree = 1
     /   \
    2     3
  /   \     \
 4     5     6
     /   \
    7     8

Sample Output
true
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inOrderTraversal(node):
    if node is None:
        return {
            'height': 0,
            'isBalanced': True
        }

    leftChild = inOrderTraversal(node.left)
    rightChild = inOrderTraversal(node.right)

    return {
        'height': max(rightChild['height'], leftChild['height']) + 1,
        'isBalanced': leftChild['isBalanced'] and rightChild['isBalanced'] and abs(rightChild['height'] - leftChild['height']) <= 1
    }


def heightBalancedBinaryTree(tree):
    result = inOrderTraversal(tree)
    return result['isBalanced']


if __name__ == "__main__":
    # TODO
    pass
