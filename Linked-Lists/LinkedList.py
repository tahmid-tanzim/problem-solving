#!/usr/bin/python3

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def __str__(self):
        return f'{self.data}'

    def __eq__(self, val):
        return self.data == val


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        output = str()
        current_node = self.head
        while current_node is not None:
            output += f'[{current_node}]~>'
            current_node = current_node.next
        return output + 'NULL'

    def __eq__(self, array) -> bool:
        current_node = self.head
        while current_node is not None:
            data = array.pop(0)
            if current_node.data != data:
                return False
            current_node = current_node.next
        return len(array) == 0

    def __get__(self):
        return self.head

    def __set__(self, head):
        self.head = head

    def appendToTail(self, val) -> None:
        last_node = Node(val)
        if self.head is None:
            self.head = last_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = last_node

    def deleteNode(self, val) -> bool:
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



