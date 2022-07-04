#!/usr/bin/python3
# https://leetcode.com/problems/delete-node-in-a-bst/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}"


class Solution1:
    def getMinValueNode(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        while node.left is not None:
            node = node.left
        return node

    def getMaxValueNode(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        while node.right is not None:
            node = node.right
        return node

    def deleteNode(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Case 1: Deleting a node with no child. i.e. deleting leaf node
        Case 2: Deleting a node with only One child. i.e. either left or right
        Case 3: Deleting a node with both left or right child.
        """
        if node is None:
            return None
        elif key < node.val:
            node.left = self.deleteNode(node.left, key)
        elif key > node.val:
            node.right = self.deleteNode(node.right, key)
        else:
            if node.left is None:  # Case 1 & Case 2
                return node.right
            elif node.right is None:  # Case 2
                return node.left
            else:  # Case 3

                # maxNodeInLeft = self.getMaxValueNode(node.left)
                # node.val = maxNodeInLeft.val
                # node.left = self.deleteNode(node.left, maxNodeInLeft.val)

                minNodeInRight = self.getMinValueNode(node.right)
                node.val = minNodeInRight.val
                node.right = self.deleteNode(node.right, minNodeInRight.val)
        return node


def preorder(node: Optional[TreeNode]):
    if node is None:
        return
    print(node)
    preorder(node.left)
    preorder(node.right)


if __name__ == "__main__":
    tree1 = TreeNode(val=10)

    tree1.left = TreeNode(
        val=5,
        left=TreeNode(val=3, left=TreeNode(val=1), right=TreeNode(val=4)),
        right=TreeNode(val=8, left=TreeNode(val=6, left=None, right=TreeNode(7)), right=TreeNode(val=9))
    )

    tree1.right = TreeNode(
        val=20,
        left=TreeNode(val=15)
    )

    obj = Solution1()
    resultRootNode = obj.deleteNode(tree1, 10)
    preorder(resultRootNode)
