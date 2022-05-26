#!/usr/bin/python3
"""
Dijkstra's Algorithm

Single-Source - Shortest Path (SSSP)
Greedy Method
Time complexity - O(n^2)
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
        # Initialize Vertex Distance
        distance = {vertex: sys.maxsize for vertex in vertices}
        distance[startVertex] = 0

        # Initialize Vertex Visited
        visited = {vertex: False for vertex in vertices}

        n = len(vertices)
        while n > 0:
            fromVertex = min(distance, key=lambda v: distance[v] if not visited[v] else sys.maxsize)
            visited[fromVertex] = True

            for toVertex, edgeWeight in self.adjacencyList[fromVertex]:
                if not visited[toVertex] and distance[fromVertex] + edgeWeight < distance[toVertex]:
                    distance[toVertex] = distance[fromVertex] + edgeWeight
            n -= 1
        return distance


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

    test_passed = 0
    for idx, val in enumerate(inputs):
        graph_obj = Graph(val["vertices"], val["edges"], val["type"])
        output = graph_obj.calculateShortestPath(val["start_vertex"], val["vertices"])
        print(output)
        # if output == val['expected']:
        #     print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
        #     test_passed += 1
        # else:
        #     print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
