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

    def __get__(self):
        return self.head

    def appendToTail(self, d) -> None:
        last_node = Node(d)
        if self.head is None:
            self.head = last_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = last_node

    def deleteNode(self, d) -> bool:
        if self.head is None:
            return False

        if self.head.data == d:
            self.head = self.head.next
            return True

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == d:
                current_node.next = current_node.next.next
                return True
            current_node = current_node.next

        return False



