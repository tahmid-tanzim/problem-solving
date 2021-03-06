#!/usr/bin/python3
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructBT(self, postorder: List[int], i: int, n: int, inorder: List[int], iStart: int, iEnd: int) -> TreeNode:
        # Base Case
        if iStart >= iEnd or i < n:
            return

        # Find Root Node
        rootValue = None
        for x in range(i, n, -1):
            if postorder[x] in inorder[iStart:iEnd]:
                rootValue = postorder[x]
                i = x
                break

        rootIdx = inorder.index(rootValue)
        root = TreeNode(rootValue)
        root.left = self.constructBT(postorder, i, n, inorder, iStart, rootIdx)
        root.right = self.constructBT(postorder, i, n, inorder, rootIdx + 1, iEnd)
        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.constructBT(postorder, len(postorder) - 1, -1, inorder, 0, len(inorder))


def order(node):
    if node is None:
        return
    print(node.val, end='-')
    order(node.left)
    order(node.right)


if __name__ == "__main__":
    s = Solution()
    # pre = [1, 2, 4, 8, 9, 10, 11, 5, 3, 6, 7]
    # ino = [8, 4, 10, 9, 11, 2, 5, 1, 6, 3, 7]
    # pre = [3, 9, 20, 15, 7]
    post = [9, 15, 7, 20, 3]
    ino = [9, 3, 15, 20, 7]
    tree = s.buildTree(ino, post)
    order(tree)
