#!/usr/bin/python3
# https://leetcode.com/problems/merge-two-binary-trees/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # def print_in_order(self):
    #     print(self.val)
    #     if self.left is not None:
    #         self.left.print_in_order()
    #     if self.right is not None:
    #         self.right.print_in_order()


def print_in_order(root):
    print(root.val)
    if root.left is not None:
        print_in_order(root.left)
    if root.right is not None:
        print_in_order(root.right)


def merge_trees(t1, t2):
    print(t1.val, t2.val)
    if root.left is not None:
        print_in_order(root.left)
    if root.right is not None:
        print_in_order(root.right)


if __name__ == '__main__':
    t1 = TreeNode(1)
    t12 = TreeNode(2)
    t13 = TreeNode(3)
    t15 = TreeNode(5)

    t13.left = t15
    t1.left = t13
    t1.right = t12
    # t1.print_in_order()
    print_in_order(t1)

    print('#############################')

    t2 = TreeNode(2)
    t21 = TreeNode(1)
    t23 = TreeNode(3)
    t24 = TreeNode(4)
    t27 = TreeNode(7)

    t21.right = t24
    t23.right = t27
    t2.left = t21
    t2.right = t23

    # t2.print_in_order()
    print_in_order(t2)
    # merge_trees(None, None)
