#!/usr/bin/python3

from Node import Node


class Graph:
    def __init__(self, adjacency_list=[]):
        noOfNodes = len(adjacency_list)
        nodes = [Node(name) for name in range(noOfNodes)]
        for node in nodes:
            for childIdx in adjacency_list[node.getName()]:
                node.addChildren(nodes[childIdx])
        self.nodes = nodes

    def __str__(self):
        result = []
        for n in self.nodes:
            result.append(f'\nRoot {n}\n\tChild {n.printChildren()}\n')
        return ''.join(result)

    def totalNodes(self):
        return len(self.nodes)

    def getNodes(self):
        return self.nodes

    def getNode(self, index):
        return self.nodes[index]
