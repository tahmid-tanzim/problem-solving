#!/usr/local/bin/python3.6

"""
https://leetcode.com/problems/binary-tree-paths/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(array):
    root = TreeNode(array[0])
    queue = [(0, root)]

    while len(queue) > 0:
        (i, p) = queue.pop(0)
        li = i * 2 + 1
        ri = i * 2 + 2
        if li < len(array) and array[li] is not None:
            t = TreeNode(array[li])
            p.left = t
            queue.append((li, t))
        if ri < len(array) and array[ri] is not None:
            t = TreeNode(array[ri])
            p.right = t
            queue.append((ri, t))
    return root


def inorder_traversal_recursive(root):
    if root:
        inorder_traversal_recursive(root.left)
        inorder_traversal_recursive(root.right)
        print(root.val)


def binary_tree_paths(root, path_string=""):
    # Base Case
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [path_string + str(root.val)]

    path_string += str(root.val) + '->'
    left_arr = binary_tree_paths(root.left, path_string)
    right_arr = binary_tree_paths(root.right, path_string)
    return left_arr + right_arr


if __name__ == "__main__":
    tree_array = [1, 2, 3, None, 5]
    root_node = create_binary_tree(tree_array)
    # inorder_traversal_recursive(root_node)
    print(binary_tree_paths(root_node))
