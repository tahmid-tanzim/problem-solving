#!/usr/bin/python3
"""
Dijkstra's Algorithm

Single-Source - Shortest Path (SSSP)
Greedy Method
Remarks - Dijkstra's algorithm may NOT work for negative weight edges
"""
import sys
from enum import Enum
from typing import List, Tuple


class EdgeType(Enum):
    DIRECTED = "Directed Graph"
    UNDIRECTED = "Undirected Graph"


class Graph:
    def __init__(self, vertices: Tuple, edges: List[Tuple], edgeType: EdgeType):
        self.adjacencyList = {vertex: [] for vertex in vertices}

        for sourceVertex, destinationVertex, edgeWeight in edges:
            self.adjacencyList[sourceVertex].append([destinationVertex, edgeWeight])
            if edgeType == EdgeType.UNDIRECTED:
                self.adjacencyList[destinationVertex].append([sourceVertex, edgeWeight])

    def calculateShortestPath(self, startVertex: str, vertices: Tuple) -> dict:
        """
        Time Complexity - O(n^2)
        Space Complexity - O(n)
        """
        minDistance, shortestPath, visited = {}, {}, {}

        for v in vertices:
            minDistance[v] = sys.maxsize
            shortestPath[v] = ""
            visited[v] = False

        minDistance[startVertex] = 0

        n = len(vertices) - 1
        while n > 0:
            fromVertex = min(minDistance, key=lambda x: minDistance[x] if not visited[x] else sys.maxsize)
            visited[fromVertex] = True

            for toVertex, edgeWeight in self.adjacencyList[fromVertex]:
                if not visited[toVertex] and minDistance[fromVertex] + edgeWeight < minDistance[toVertex]:
                    minDistance[toVertex] = minDistance[fromVertex] + edgeWeight
                    shortestPath[toVertex] = shortestPath[fromVertex][:-1] + fromVertex + toVertex
            n -= 1

        shortestPathWithDistance = {
            v: dict(
                distance=minDistance[v],
                path=shortestPath[v]
            )
            for v in vertices
        }
        return shortestPathWithDistance


if __name__ == "__main__":
    inputs = (
        {
            "start_vertex": "A",
            "vertices": ("A", "B", "C", "D", "E", "F"),
            "edges": [
                ("A", "B", 2),
                ("A", "C", 4),
                ("B", "C", 1),
                ("B", "D", 7),
                ("C", "E", 3),
                ("D", "F", 1),
                ("E", "F", 5),
                ("E", "D", 2),
            ],
            "type": EdgeType.DIRECTED,
        },
        {
            "start_vertex": "A",
            "vertices": ("A", "B", "C", "D", "E", "F"),
            "edges": [
                ("A", "B", 50),
                ("A", "D", 10),
                ("A", "C", 45),
                ("B", "C", 10),
                ("B", "D", 15),
                ("C", "E", 30),
                ("D", "A", 10),
                ("D", "E", 15),
                ("E", "B", 20),
                ("E", "C", 35),
                ("F", "E", 3),
            ],
            "type": EdgeType.DIRECTED,
        },
        {
            "start_vertex": "A",
            "vertices": ("A", "B", "C", "D", "E", "F", "G", "H", "I"),
            "edges": [
                ("A", "B", 4),
                ("A", "H", 8),
                ("H", "B", 11),
                ("B", "C", 8),
                ("H", "I", 7),
                ("H", "G", 1),
                ("I", "G", 6),
                ("I", "C", 2),
                ("D", "C", 7),
                ("D", "E", 9),
                ("D", "F", 14),
                ("E", "F", 10),
                ("C", "F", 4),
                ("G", "F", 2),
            ],
            "type": EdgeType.UNDIRECTED,
        },
    )

    for idx, val in enumerate(inputs):
        graph_obj = Graph(val["vertices"], val["edges"], val["type"])
        output = graph_obj.calculateShortestPath(val["start_vertex"], val["vertices"])
        print(f"{idx}.", "\n{")
        for key, value in output.items():
            print(f"\t{key}: {value},")
        print("}\n")

