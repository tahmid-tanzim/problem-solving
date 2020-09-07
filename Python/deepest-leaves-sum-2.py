#!/usr/local/bin/python3
# https://leetcode.com/problems/deepest-leaves-sum/


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


# BFS Approach
def deepest_leaves_sum(root):
    if root is None:
        return []
    queue = [(root, 0)]
    level_order = []
    while queue:
        (i, level) = queue.pop(0)
        if level < len(level_order):  # Existing Row
            level_order[level].append(i.val)
        else:  # New Row
            level_order.append([i.val])
        # print(f'VISITED {i.val} - Level {level}')
        li, ri = i.left, i.right
        level += 1
        if li is not None:
            queue.append((li, level,))
        if ri is not None:
            queue.append((ri, level,))
    return sum(level_order[-1])


if __name__ == "__main__":
    # tree_array = [3, 9, 20, None, None, 15, 7]  # FALSE
    # tree_array = [10, 5, 15, None, None, 6, 20]
    tree_array = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, None, None, 8]
    # tree_array = [2, 1, 3]
    root_node = create_binary_tree(tree_array)
    print(deepest_leaves_sum(root_node))
