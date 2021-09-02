#!/usr/bin/python3
# https://leetcode.com/problems/deepest-leaves-sum/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.val}'


def create_binary_tree(array: list) -> TreeNode:
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


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)


# Using One Stack
def post_order_iter1(root):
    i = root
    stack = [root]
    while len(stack) > 0 or i is not None:
        while i.left is not None:
            stack.append(i.left)
            i = i.left
        if i.right is not None:
            stack.append(i.right)
            i = i.right
        else:
            # stack.append(i)
            visited = stack.pop()
            print(visited.val)
            if stack:
                i = stack[-1]
            else:
                break


def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None


# Using Two Stack
def post_order_iter2(root):
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

    # return ans
    print(ans)


def max_depth(root: TreeNode) -> int:
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":
    tree_array = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, None, None, 8]
    root_node = create_binary_tree(tree_array)
    post_order_iter2(root_node)
    # print(max_depth(root_node))
