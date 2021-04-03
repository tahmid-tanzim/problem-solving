#!/usr/bin/python3

from TreeNode import TreeNode


def preOrderTraversal(root) -> None:
    if root:
        print(root.name)
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)


def inOrderTraversal(root) -> None:
    if root:
        inOrderTraversal(root.left)
        print(root.name)
        inOrderTraversal(root.right)


def createMinimalBST(arr: list, start: int, end: int) -> TreeNode:
    if start > end:
        return None

    mid = start + (end - start) // 2
    new_node = TreeNode(arr[mid])
    new_node.addLeft(createMinimalBST(arr, start, mid - 1))
    new_node.addRight(createMinimalBST(arr, mid + 1, end))
    return new_node


if __name__ == "__main__":
    array = [1, 2, 4, 6, 8, 10, 12, 14]
    root_node = createMinimalBST(array, 0, len(array) - 1)
    inOrderTraversal(root_node)
