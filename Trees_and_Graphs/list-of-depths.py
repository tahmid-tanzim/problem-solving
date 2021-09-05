#!/usr/bin/python3
# Cracking the Coding Interview - Trees and Graphs - 4.3. List of Depths
from TreeNode import TreeNode


class LinkedListNode:
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data}'


def levelOrderTraverse(node: TreeNode, lists, level: int):
    if node is None:
        return

    if len(lists) == level:
        lists.append(LinkedListNode(node.getName()))
    else:
        head = lists[level]
        while head.next is not None:
            head = head.next
        head.next = LinkedListNode(node.getName())

    levelOrderTraverse(node.left, lists, level + 1)
    levelOrderTraverse(node.right, lists, level + 1)


if __name__ == "__main__":
    # Tree Initialization
    root_node = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n9 = TreeNode(9)

    n8.addLeft(n9)
    n5.addLeft(n7)
    n5.addRight(n8)
    n3.addLeft(n5)
    n4.addRight(n6)
    n2.addLeft(n4)
    root_node.addLeft(n2)
    root_node.addRight(n3)

    levelLinkedLists = list()
    levelOrderTraverse(root_node, levelLinkedLists, 0)

    i = 0
    for ll in levelLinkedLists:
        print("Level - ", i, end=" | ")
        while ll is not None:
            print(f"{ll}->", end='')
            ll = ll.next
        print(f"Null")
        i += 1
