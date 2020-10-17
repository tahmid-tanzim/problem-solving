#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/search-in-a-binary-search-tree/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'Node val - {self.val}'


def searchBST(root: TreeNode, val: int) -> TreeNode:
    if root is None:
        return None

    if root.val == val:
        return root

    root.left = searchBST(root.left, val)
    root.right = searchBST(root.right, val)
    return root.left or root.right


if __name__ == '__main__':
    r = TreeNode(4)
    n2 = TreeNode(2)
    n7 = TreeNode(7)
    n1 = TreeNode(1)
    n3 = TreeNode(3)

    n2.left = n1
    n2.right = n3

    r.left = n2
    r.right = n7

    subtree_root = searchBST(r, 2)
    print('Result - ', subtree_root)
