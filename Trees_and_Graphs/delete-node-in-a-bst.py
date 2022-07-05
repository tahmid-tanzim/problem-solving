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


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val: int):
        new_node = TreeNode(val=val)
        if self.root is None:
            self.root = new_node
            return
        
        def add_node(current_node):
            if val < current_node.val:
                if current_node.left is None:
                    current_node.left = new_node
                    return 
                else:
                    add_node(current_node.left)
            elif val >= current_node.val:
                if current_node.right is None:
                    current_node.right = new_node
                    return 
                else:
                    add_node(current_node.right)
        
        add_node(self.root)
        

# Time Complexity - O(h). Where h is the height of BST
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

    preorder(node.left)
    preorder(node.right)
    print(node)


if __name__ == "__main__":
    bst1 = BinarySearchTree()
    bst1.insert(10)
    bst1.insert(5)
    bst1.insert(20)
    bst1.insert(3)
    bst1.insert(8)
    bst1.insert(1)
    bst1.insert(4)
    bst1.insert(6)
    bst1.insert(9)
    bst1.insert(7)
    bst1.insert(15)
    tree1 = bst1.root
    #################
    bst2 = BinarySearchTree()
    bst2.insert(5)
    bst2.insert(3)
    bst2.insert(6)
    bst2.insert(7)
    bst2.insert(2)
    bst2.insert(4)
    tree2 = bst2.root
    #################
    obj = Solution1()
    resultRootNode = obj.deleteNode(tree2, 3)
    preorder(resultRootNode)
    
