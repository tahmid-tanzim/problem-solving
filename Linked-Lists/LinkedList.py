#!/usr/bin/python3
from typing import List


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data}'

    def __eq__(self, val):
        return self.data == val


class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head

    def __repr__(self):
        output = str()
        current_node = self.head
        while current_node is not None:
            output += f'[{current_node}]~>'
            current_node = current_node.next
        return output + 'NULL'

    def __eq__(self, array: List[int]) -> bool:
        i = 0
        n = len(array)
        current_node = self.head
        while current_node is not None:
            if i >= n or current_node.data != array[i]:
                return False
            current_node = current_node.next
            i += 1
        return i == n

    def __get__(self):
        return self.head

    def __set__(self, head: Node):
        self.head = head

    def appendToTail(self, val: int) -> None:
        last_node = Node(val)
        if self.head is None:
            self.head = last_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = last_node

    def appendNodeToTail(self, last_node: Node) -> None:
        if self.head is None:
            self.head = last_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = last_node

    def deleteNode(self, val: int) -> bool:
        if self.head is None:
            return False

        if self.head.data == val:
            self.head = self.head.next
            return True

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == val:
                current_node.next = current_node.next.next
                return True
            current_node = current_node.next

        return False

    def deleteMiddle(self):
        if self.head is None:
            return

        if self.head.next is None or self.head.next.next is None:
            self.head = self.head.next
            return

        fast = self.head
        slow = None
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = self.head if slow is None else slow.next

        slow.next = slow.next.next
