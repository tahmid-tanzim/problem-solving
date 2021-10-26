#!/usr/bin/python3
# https://www.youtube.com/playlist?list=PL_z_8CaSLPWfxJPz2-YKqL9gXWdgrhvdn
# https://leetcode.com/problems/diameter-of-binary-tree/
# Dynamic Programming on Tree
# DP on Tree
from TreeNode import create_binary_tree


class Solution:
    def __init__(self):
        self._result = float("-inf")

    def calculateDiameterOfBinaryTree(self, root) -> int:
        """
        ~> maximum number of nodes between 2 leaf nodes
        """
        if root is None:
            return 0

        left_number_of_nodes = self.calculateDiameterOfBinaryTree(root.left)
        right_number_of_nodes = self.calculateDiameterOfBinaryTree(root.right)
        max_number_of_nodes = 1 + max(left_number_of_nodes, right_number_of_nodes)
        diameter_of_2_leaf = max(max_number_of_nodes, 1 + left_number_of_nodes + right_number_of_nodes)
        self._result = max(self._result, diameter_of_2_leaf)
        return max_number_of_nodes

    def diameterOfBinaryTree(self, root) -> int:
        self.calculateDiameterOfBinaryTree(root)
        return int(self._result) - 1


if __name__ == "__main__":
    tree_array = [1, 2, 3, 4, 5]
    root_node = create_binary_tree(tree_array)
    obj = Solution()
    print(obj.diameterOfBinaryTree(root_node))
