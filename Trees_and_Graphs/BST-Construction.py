#!/usr/bin/python3
# https://www.algoexpert.io/questions/BST%20Construction


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    def remove(self, value, parentNode=None):
        if value < self.value and self.left is not None:
            self.left.remove(value, self)
        elif value > self.value and self.right is not None:
            self.right.remove(value, self)
        else:
            """(self.value == value)"""
            if self.left is not None and self.right is not None:
                parentNode = self
                tempNode = self.right
                while tempNode.left is not None:
                    parentNode = tempNode
                    tempNode = tempNode.left

                self.value = tempNode.value
                parentNode.left = None
            elif self.left is not None and self.right is None:
                parentNode.left = self.left
            elif self.left is None and self.right is not None:
                parentNode.right = self.right
            else:
                if parentNode.left is not None:
                    if parentNode.left.value == value:
                        parentNode.left = None
                if parentNode.right is not None:
                    if parentNode.right.value == value:
                        parentNode.right == None

        return self


if __name__ == "__main__":
    # TODO
    pass
