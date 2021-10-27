#!/usr/bin/python3
# https://www.youtube.com/playlist?list=PL_z_8CaSLPWfxJPz2-YKqL9gXWdgrhvdn
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# https://www.algoexpert.io/questions/Max%20Path%20Sum%20In%20Binary%20Tree
from TreeNode import TreeNode, create_binary_tree


class Solution:
    """
    0. Node value can be (-ve) negative
    1. Any node to any node
    2. Doesn't necessary to include leaf nodes
    3. Doesn't necessary to pass through root node
    """

    def __init__(self):
        self._maxPathSumValue = float("-inf")

    def calculateMaxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0

        leftMPS = max(0, self.calculateMaxPathSum(root.left))
        rightMPS = max(0, self.calculateMaxPathSum(root.right))

        self._maxPathSumValue = max(self._maxPathSumValue, root.val + leftMPS + rightMPS)
        return root.val + max(leftMPS, rightMPS)

    def maxPathSum(self, root: TreeNode) -> int:
        self.calculateMaxPathSum(root)
        return int(self._maxPathSumValue)


if __name__ == "__main__":
    # tree_array = [-10, 9, 20, None, None, 15, 7]
    tree_array = [10, 2, 11, 20, 1, None, -25, None, None, None, None, None, None, 3, 4]
    root_node = create_binary_tree(tree_array)

    obj = Solution()
    output = obj.maxPathSum(root_node)
    print("Valid output - 42\nActual output -", output)
