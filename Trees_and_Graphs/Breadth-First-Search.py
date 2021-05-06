#!/usr/bin/python3

from Graph import Graph
from Node import Node


def breadthFirstSearch(root: Node):
    queue = list()
    root.setState(True)
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        print(f'VISIT {node}')
        for child in node.getChildren():
            if child.isState(False):
                child.setState(True)
                queue.append(child)


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
    print(f'BFS - {breadthFirstSearch(graph.getNode(0))}\n')
