#!/usr/bin/python3
# https://www.algoexpert.io/questions/Depth-first%20Search
"""
GRAPH
              A
          /   |   \
        B     C    D
    /      \     /    \
   E        F   G      H
          /  \   \
         I    J   K

OUTPUT = ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
"""


# O(v+e) time
# O(v) space
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


if __name__ == "__main__":
    # TODO
    pass
