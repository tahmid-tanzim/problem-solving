#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/maximum-depth-of-binary-tree/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 1
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    def findDepth(self, root: int) -> int:
        if root == 0:
            return 0
        root -= 1
        return 1 + self.findDepth(root)


if __name__ == '__main__':
    r = TreeNode(3)
    n9 = TreeNode(9)
    n20 = TreeNode(20)
    n15 = TreeNode(15)
    n7 = TreeNode(7)

    # x = TreeNode(1)
    # n7.right = x

    n20.left = n15
    n20.right = n7

    r.left = n9
    r.right = n20

    s = Solution()

    # depth = s.maxDepth(r)
    # print('LAST: ', depth)
    # print('Find Depth: ', s.findDepth(5))
    print('Find Depth: ', s.minDepth(r))
