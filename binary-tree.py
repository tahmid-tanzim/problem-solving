#!/usr/bin/python3


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, value):
        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.data:
            return True
        elif value <= self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def print_in_order(self):
        if self.left is not None:
            self.left.print_in_order()
        print(self.data)
        if self.right is not None:
            self.right.print_in_order()


root = Node(10)
root.insert(5)
root.insert(15)
root.insert(8)
root.insert(17)
root.insert(12)
print('Is 8 exist: ', root.contains(8))
print('Is 12 exist: ', root.contains(12))
root.print_in_order()
