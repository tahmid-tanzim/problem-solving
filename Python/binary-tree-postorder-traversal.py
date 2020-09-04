#!/usr/local/bin/python3
# https://leetcode.com/problems/binary-tree-postorder-traversal/


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
        li = i + 1
        ri = i + 2
        if li < len(array) and array[li] is not None:
            t = TreeNode(array[li])
            p.left = t
            queue.append((li, t))
        if ri < len(array) and array[ri] is not None:
            t = TreeNode(array[ri])
            p.right = t
            queue.append((ri, t))
    return root


def postorder_traversal_recursive(root):
    if root:
        postorder_traversal_recursive(root.left)
        postorder_traversal_recursive(root.right)
        print(root.val)


def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None


# using 2 stack
def postorder_traversal_iterative(root):
    if root is None:
        return

    stack = []
    ans = []
    while True:
        while root:
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
            root = root.left
        root = stack.pop()

        if root.right is not None and peek(stack) == root.right:
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            ans.append(root.val)
            root = None

        if len(stack) <= 0:
            break

    return ans


if __name__ == "__main__":
    tree_array = [1, None, 2, 3]
    root_node = create_binary_tree(tree_array)
    # postorder_traversal_recursive(root_node)
    print(postorder_traversal_iterative(root_node))
