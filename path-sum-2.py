#!/usr/local/bin/python3.6

"""
https://leetcode.com/problems/path-sum-ii/
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
        print(root.val)
        inorder_traversal_recursive(root.left)
        inorder_traversal_recursive(root.right)


def inorder_traversal_iterative(root):
    stack = []
    output = []
    while len(stack) > 0 or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print(root.val)
            output.append(root.val)
            root = root.right
    return output


def path_sum(root, sum, paths):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [[root.val]] if sum == root.val else []

    sum -= root.val

    left_arr = path_sum(root.left, sum, paths)
    right_arr = path_sum(root.right, sum, paths)

    paths = left_arr + right_arr

    for path in paths:
        path.insert(0, root.val)
    return paths


if __name__ == "__main__":
    tree_array = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]
    root_node = create_binary_tree(tree_array)
    # inorder_traversal_recursive(root_node)
    print(path_sum(root_node, 22, []))