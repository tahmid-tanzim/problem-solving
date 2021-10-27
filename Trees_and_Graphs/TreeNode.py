#!/usr/bin/python3


class TreeNode:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.val = name
        self.left = left
        self.right = right

    def __str__(self):
        return f'Node {self.name}'

    def __eq__(self, val):
        return self.name == val

    def getName(self):
        return self.name

    def getValue(self):
        return self.val

    def addLeft(self, left):
        self.left = left

    def addRight(self, right):
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
