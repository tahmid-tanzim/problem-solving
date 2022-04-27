#!/usr/bin/python3
# https://leetcode.com/problems/recover-binary-search-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.x = None
        self.y = None

    def helper(self, node: Optional[TreeNode], left_range: int, right_range: int):
        if node is None:
            return

        if left_range <= node.val <= right_range:
            self.helper(node.left, pow(-2, 31), node.val)
            self.helper(node.right, node.val, pow(2, 31) - 1)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.helper(root.left, pow(-2, 31), root.val)
        self.helper(root.right, root.val, pow(2, 31) - 1)
