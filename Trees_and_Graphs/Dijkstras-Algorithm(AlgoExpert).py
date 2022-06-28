#!/usr/bin/python3
# https://www.algoexpert.io/questions/Dijkstra's%20Algorithm
"""
  You're given an integer start and a list edges of
  pairs of integers.

  The list is what's called an adjacency list, and it represents a graph. The
  number of vertices in the graph is equal to the length of edges,
  where each index i in edges contains vertex
  i's outbound edges, in no particular order. Each individual edge
  is represented by an pair of two numbers,
  [destination, distance], where the destination is a positive
  integer denoting the destination vertex and the distance is a positive integer
  representing the length of the edge (the distance from vertex
  i to vertex destination). Note that these edges are
  directed, meaning that you can only travel from a particular vertex to its
  destination—not the other way around (unless the destination vertex itself has
  an outbound edge to the original vertex).

  Write a function that computes the lengths of the shortest paths between
  start and all of the other vertices in the graph using Dijkstra's
  algorithm and returns them in an array. Each index i in the
  output array should represent the length of the shortest path between
  start and vertex i. If no path is found from
  start to vertex i, then output[i] should be -1.

  Note that the graph represented by edges won't contain any
  self-loops (vertices that have an outbound edge to themselves) and will only
  have positively weighted edges (i.e., no negative distances).

  If you're unfamiliar with Dijkstra's algorithm, we recommend watching the
  Conceptual Overview section of this question's video explanation before starting to code.

Sample Input
start = 0
edges = [
  [[1, 7]],
  [[2, 6], [3, 20], [4, 3]],
  [[3, 14]],
  [[4, 2]],
  [],
  [],
]

Sample Output
[0, 7, 13, 27, 10, -1]
"""


# Time Complexity - O((v+e) * log(v))
# Space Complexity - O(v)
def getNotVisitedMinValue(visited, shortest_path):
    min_val = [0, float('inf')]
    for i in range(len(shortest_path)):
        if shortest_path[i] <= min_val[1] and not visited[i]:
            min_val[0] = i
            min_val[1] = shortest_path[i]
    return min_val


# O(v^2 + e) time | O(v) space
def dijkstrasAlgorithm(start, edges):
    total_vertices = len(edges)
    shortest_path = [float('inf') for _ in range(total_vertices)]
    shortest_path[start] = 0

    visited = [False for _ in range(total_vertices)]

    for _ in range(total_vertices):
        [min_index, min_value] = getNotVisitedMinValue(visited, shortest_path)
        if min_value == float('inf'):
            break
        visited[min_index] = True
        for adjacent_vertices in edges[min_index]:
            if visited[adjacent_vertices[0]]:
                continue
            if min_value + adjacent_vertices[1] < shortest_path[adjacent_vertices[0]]:
                shortest_path[adjacent_vertices[0]] = min_value + adjacent_vertices[1]

    for j in range(total_vertices):
        if shortest_path[j] == float('inf'):
            shortest_path[j] = -1

    return shortest_path


if __name__ == "__main__":
    print(dijkstrasAlgorithm(start=0,
                             edges=[
                                 [[1, 7]],
                                 [[2, 6], [3, 20], [4, 3]],
                                 [[3, 14]],
                                 [[4, 2]],
                                 [],
                                 [],
                             ]))
