#!/usr/bin/python3
# https://www.algoexpert.io/questions/Cycle%20In%20Graph
"""
  You're given a list of edges representing an unweighted, directed
  graph with at least one node. Write a function that returns a boolean
  representing whether the given graph contains a cycle.

  For the purpose of this question, a cycle is defined as any number of
  vertices, including just one vertex, that are connected in a closed chain. A
  cycle can also be defined as a chain of at least one vertex in which the first
  vertex is the same as the last.

  The given list is what's called an adjacency list, and it represents a graph.
  The number of vertices in the graph is equal to the length of
  edges, where each index i in edges contains vertex i's outbound edges, in no
  particular order. Each individual edge is represented by a positive integer
  that denotes an index (a destination vertex) in the list that this vertex is
  connected to. Note that these edges are directed, meaning that you can only
  travel from a particular vertex to its destination, not the other way around
  (unless the destination vertex itself has an outbound edge to the original vertex).

  Also note that this graph may contain self-loops. A self-loop is an edge that
  has the same destination and origin; in other words, it's an edge that
  connects a vertex to itself. For the purpose of this question, a self-loop is considered a cycle.

  For a more detailed explanation, please refer to the Conceptual Overview
  section of this question's video explanation.

Sample Input
edges = [
  [1, 3],
  [2, 3, 4],
  [0],
  [],
  [2, 5],
  [],
]

Sample Output
true 
// There are multiple cycles in this graph: 
// 1) 0 -> 1 -> 2 -> 0
// 2) 0 -> 1 -> 4 -> 2 -> 0
// 3) 1 -> 2 -> 0 -> 1
// These are just 3 examples; there are more.
"""


# DFS
def isNodeInCycle(edges, node, visited, stack):
    visited[node] = True
    stack[node] = True

    for neighbor in edges[node]:
        if not visited[neighbor]:
            containsCycle = isNodeInCycle(edges, neighbor, visited, stack)
            if containsCycle:
                return True
        elif stack[neighbor]:
            return True

    stack[node] = False
    return False


def cycleInGraph(edges):
    numberOfNodes = len(edges)
    visited = [False for _ in range(numberOfNodes)]
    stack = [False for _ in range(numberOfNodes)]

    for node in range(numberOfNodes):
        if not visited[node]:
            containsCycle = isNodeInCycle(edges, node, visited, stack)
            if containsCycle:
                return True

    return False


if __name__ == "__main__":

    inputs = (
        {
            "edges": [
                [1, 3],
                [2, 3, 4],
                [0],
                [],
                [2, 5],
                []
            ],
            "expected": True
        },
        {
            "edges": [
                [1, 2],
                [2],
                []
            ],
            "expected": False
        },
        {
            "edges": [
                [],
                [0, 2],
                [0, 3],
                [0, 4],
                [0, 5],
                [0]
            ],
            "expected": False
        },
        {
            "edges": [
                [1],
                [2, 3, 4, 5, 6, 7],
                [],
                [2, 7],
                [5],
                [],
                [4],
                []
            ],
            "expected": False
        },

        {
            "edges": [[], [0]],
            "expected": False
        },
        {
            "edges": [[1], [0]],
            "expected": True
        },
        {
            "edges": [[1, 3], [2, 3, 4], [0], [], [2, 5], []],
            "expected": True
        },
        {
            "edges": [[1], [2, 3, 4, 5, 6, 7], [], [2, 7], [5], [], [4], []],
            "expected": False
        },
        {
            "edges": [[1, 2], [2], [3], []],
            "expected": False
        },
        {
            "edges": [[3], [3, 4], [4, 7], [5, 6, 7], [6], [], [], [0]],
            "expected": True
        },
        {
            "edges": [[], [0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10],
                      [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19],
                      [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28],
                      [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [34, 35], [35, 36], [36, 37],
                      [37, 38], [38, 39], [39, 40], [40, 41], [41, 42], [42, 43], [43, 44], [44, 45], [45, 46],
                      [46, 47], [47, 48], [48, 49], [49, 50], [50, 51], [51, 52], [52, 53], [53, 54], [54, 55],
                      [55, 56], [56, 57], [57, 58], [58, 59], [59, 60], [60, 61], [61, 62], [62, 63], [63, 64],
                      [64, 65], [65, 66], [66, 67], [67, 68], [68, 69], [69, 70], [70, 71], [71, 72], [72, 73],
                      [73, 74], [74, 75], [75, 76], [76, 77], [77, 78], [78, 79], [79, 80], [80, 81], [81, 82],
                      [82, 83], [83, 84], [84, 85], [85, 86], [86, 87], [87, 88], [88, 89], [89, 90], [90, 91],
                      [91, 92], [92, 93], [93, 94], [94, 95], [95, 96], [96, 97], [97]],
            "expected": False
        }
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = cycleInGraph(val["edges"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
