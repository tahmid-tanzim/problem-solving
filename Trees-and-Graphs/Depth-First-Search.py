#!/usr/bin/python3

from Graph import Graph
from Node import Node


def depthFirstSearch(root: Node):
    if root is None:
        return

    print(f'VISIT {root}')
    root.setState(True)

    for child in root.getChildren():
        if child.isState(False):
            depthFirstSearch(child)


if __name__ == "__main__":
    """
    (0) -> (1) <- (2)
     |  \   |  \   ^
     V  _\  V   _\ |
    (5)    (4) <- (3)
    """
    adjacencyList = [
        [1, 4, 5],
        [3, 4],
        [1],
        [2, 4],
        [],
        []
    ]
    graph = Graph(adjacencyList, False)
    # print(f'GRAPH - ', graph)
    print(f'BFS - {depthFirstSearch(graph.getNode(0))}\n')
