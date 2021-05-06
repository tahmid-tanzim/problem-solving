#!/usr/bin/python3


class TreeNode:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

    def __str__(self):
        return f'Node {self.name}'

    def __eq__(self, val):
        return self.name == val

    def getName(self):
        return self.name

    def addLeft(self, left):
        self.left = left

    def addRight(self, right):
        self.right = right
