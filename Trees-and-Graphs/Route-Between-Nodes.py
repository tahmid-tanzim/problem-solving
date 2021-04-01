#!/usr/bin/python3

from Graph import Graph
from Node import Node


def routeSearch(g: Graph, start: Node, end: Node) -> bool:
    if start == end:
        return True

    queue = list()
    for u in g.getNodes():
        u.setState('UNVISITED')

    start.setState('VISITING')
    queue.append(start)
    while len(queue) > 0:
        u = queue.pop(0)
        for v in u.getChildren():
            if v.isState('UNVISITED'):
                if v == end:
                    return True
                else:
                    v.setState('VISITING')
                    queue.append(v)
        u.setState('VISITED')
    return False


if __name__ == "__main__":
    """
    (0) -> (1) <- (2)
     |  \   |  \   ^
     V  _\  V   _\ |
    (5)    (4) <- (3)
    """
    adjacencyList = [
        [4, 5, 1],
        [4, 3],
        [1],
        [2, 4],
        [6],
        [],
        []
    ]
    graph = Graph(adjacencyList)
    # print(f'GRAPH - ', graph)
    print(f'Ans should be TRUE - {routeSearch(graph, graph.getNode(0), graph.getNode(2))}\n')
    print(f'Ans should be FALSE - {routeSearch(graph, graph.getNode(2), graph.getNode(5))}\n')
