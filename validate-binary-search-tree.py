#!/usr/local/bin/python3
# https://leetcode.com/problems/validate-binary-search-tree/


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
        li = (i * 2) + 1
        ri = (i * 2) + 2
        if li < len(array) and array[li] is not None:
            t = TreeNode(array[li])
            p.left = t
            queue.append((li, t))
        if ri < len(array) and array[ri] is not None:
            t = TreeNode(array[ri])
            p.right = t
            queue.append((ri, t))
    return root


# BFS Approach
# def is_valid_bst_bfs(root):
#     if root is None:
#         return True
#     queue = [root]
#     while queue:
#         i = queue.pop(0)
#         print(f'VISITED {i.val}')
#         li, ri = i.left, i.right
#         if li is not None:
#             if li.val >= i.val:
#                 return False
#             queue.append(li)
#         if ri is not None:
#             if i.val >= ri.val:
#                 return False
#             queue.append(ri)
#     return True

def in_order(root, stack):
    if root:
        in_order(root.left, stack)
        stack.append(root.val)
        in_order(root.right, stack)
    return stack


def is_valid_bst_dfs(root):
    stack = in_order(root, [])
    i = 1
    while i < len(stack):
        if stack[i - 1] >= stack[i]:
            return False
        i += 1
    return True


if __name__ == "__main__":
    tree_array = [10, 5, 15, None, None, 6, 20]  # FALSE
    # tree_array = [1, 1]  # FALSE
    # tree_array = [2, 1, 3]  # TRUE
    root_node = create_binary_tree(tree_array)
    print(is_valid_bst_dfs(root_node))
