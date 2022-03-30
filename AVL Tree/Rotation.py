#!/usr/bin/python3


class Node:
    __root = None

    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


def find_height(parent_node):
    left_height = parent_node.left.height if parent_node is not None and parent_node.left is not None else 0
    right_height = parent_node.right.height if parent_node is not None and parent_node.right is not None else 0
    return max(left_height, right_height) + 1


def balance_factor(parent_node):
    left_height = parent_node.left.height if parent_node is not None and parent_node.left is not None else 0
    right_height = parent_node.right.height if parent_node is not None and parent_node.right is not None else 0
    return left_height - right_height


def LLRotation(parent_node):
    """
    Before LL Rotation

            (p)
           /
        (pl)
       /   \
    (pll)  (plr)

    After LL Rotation

        (pl)
       /   \
    (pll)  (p)
          /
       (plr)
    """
    parent_left = parent_node.left
    parent_left_right = parent_left.right

    parent_left.right = parent_node
    parent_node.left = parent_left_right

    parent_node.height = find_height(parent_node)
    parent_left.height = find_height(parent_left)

    if Node.__root == parent_node:
        Node.__root = parent_left

    return parent_left


def LRRotation(parent_node):
    parent_left = parent_node.left
    parent_left_right = parent_left.right

    parent_left.right = parent_left_right.left
    parent_node.left = parent_left_right.right

    parent_left_right.left = parent_left
    parent_left_right.right = parent_node

    parent_left.height = find_height(parent_left)
    parent_node.height = find_height(parent_node)
    parent_left_right.height = find_height(parent_left_right)

    if Node.__root == parent_node:
        Node.__root = parent_left_right

    return parent_left_right


def RRRotation(parent_node):
    pass


def RLRotation(parent_node):
    pass


def insert(parent_node, data):
    if parent_node is None:
        return Node(data)

    if data < parent_node.data:
        parent_node.left = insert(parent_node.left, data)
    else:
        parent_node.right = insert(parent_node.right, data)

    parent_node.height = find_height(parent_node)
    if balance_factor(parent_node) == 2 and balance_factor(parent_node.left) == 1:
        return LLRotation(parent_node)
    elif balance_factor(parent_node) == 2 and balance_factor(parent_node.left) == -1:
        return LRRotation(parent_node)
    elif balance_factor(parent_node) == -2 and balance_factor(parent_node.right) == -1:
        return RRRotation(parent_node)
    elif balance_factor(parent_node) == -2 and balance_factor(parent_node.right) == 1:
        return RLRotation(parent_node)
    return parent_node


if __name__ == "__main__":
    """
     LL Rotation
     """
    # root = insert(None, 10)
    # Node.__root = root
    #
    # insert(root, 5)
    # insert(root, 2)
    #
    # root = Node.__root
    # print(root)

    """
    LR Rotation
    """
    root = insert(None, 50)
    Node.__root = root

    insert(root, 10)
    insert(root, 20)

    root = Node.__root
    print(root)
