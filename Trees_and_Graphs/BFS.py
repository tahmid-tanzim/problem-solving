#!/usr/bin/python3
# https://www.algoexpert.io/questions/Breadth-first%20Search
"""
GRAPH
              A
          /   |   \
        B     C    D
    /      \     /    \
   E        F   G      H
          /  \   \
         I    J   K

OUTPUT = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
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

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current is not None:
                array.append(current.name)
                queue += current.children
        return array


if __name__ == "__main__":
    # TODO
    pass
