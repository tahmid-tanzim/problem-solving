#!/usr/bin/python3
# https://leetcode.com/problems/design-linked-list/


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        head = self.head
        i = 0
        while head is not None:
            if i == index:
                return head.val if head.val is not None else -1
            i += 1
            head = head.next
        return -1

    def addAtHead(self, val: int) -> None:
        head = Node(val)
        head.next = self.head
        self.head = head
        self.size = self.size + 1

    def addAtTail(self, val: int) -> None:
        tail = Node(val)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = tail
        self.size = self.size + 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size - 1:
            self.addAtTail(val)
        elif index < self.size:
            i, node = 0, Node(val)
            current_node = self.head
            while i < index:
                current_node = current_node.next
                i += 1
            print(i, current_node.val)
            node.next = current_node
            # current_node.next = node
            # self.size = self.size + 1

    def deleteAtIndex(self, index: int) -> None:
        pass


if __name__ == '__main__':
    obj = MyLinkedList()
    obj.addAtHead(100)
    obj.addAtTail(150)
    obj.addAtTail(200)
    obj.addAtTail(250)
    obj.addAtIndex(1, 125)
    param_1 = obj.get(0)

    # print(param_1)

    # print(param_1)
    # obj.addAtHead(1)
    # obj.addAtTail(9)
    # obj.addAtIndex(1, 5)
    # obj.deleteAtIndex(2)

