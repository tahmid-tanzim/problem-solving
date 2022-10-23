#!/usr/bin/python3
# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem?isFullScreen=true
from typing import List, Tuple


class Graph:
    def __init__(self, n):
        self.noOfNodes = n
        self.adjacencyList = [[] for _ in range(n)]

    def connect(self, u, v):
        self.adjacencyList[u].append(v)
        self.adjacencyList[v].append(u)

    def find_all_distances(self, s):
        result = [-1] * self.noOfNodes
        queue = [s]
        path = set()
        # result = [0: 0, 1: 6, 2: 12, 3: 18, 4: 6, 5: -1]
        # path = (0, 1, 4, 2)
        # queue = [3]
        while len(queue) > 0:
            currentNode = queue.pop(0)
            if currentNode in path:
                continue
            path.add(currentNode)

            if result[currentNode] == -1:
                result[currentNode] = 0

            for neighbourNode in self.adjacencyList[currentNode]:
                if neighbourNode not in path:
                    result[neighbourNode] = 6 + result[currentNode]
                    queue.append(neighbourNode)
            # path.remove(currentNode)

        del result[s]
        return result


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n, m = [int(v) for v in input().split()]
        graph = Graph(n)
        for i in range(m):
            x, y = [int(v) for v in input().split()]
            graph.connect(x-1,y-1)
        s = int(input())
        a = graph.find_all_distances(s-1)
        print(' '.join([str(i) for i in a]))
