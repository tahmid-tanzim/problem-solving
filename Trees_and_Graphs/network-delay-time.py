#!/usr/bin/python3
# https://leetcode.com/problems/network-delay-time/
from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacencyList = []
        visited = []

        for i in range(n):
            adjacencyList.append([])
            visited.append(False)

        for u, v, w in times:
            # {fromNode: [(toNode, cost,)]}
            adjacencyList[u - 1].append((v - 1, w,))

        minHeap = [(0, k - 1)]  # (distance, node)
        minDelayTime = 0
        while len(minHeap) > 0:
            accumulatedTime, selectedNode = heapq.heappop(minHeap)
            if visited[selectedNode]:
                continue

            visited[selectedNode] = True
            minDelayTime = max(minDelayTime, accumulatedTime)
            for neighbourNode, edgeTime in adjacencyList[selectedNode]:
                if not visited[neighbourNode]:
                    heapq.heappush(minHeap, (edgeTime + accumulatedTime, neighbourNode))

        return minDelayTime if visited.count(True) == n else -1


if __name__ == "__main__":
    inputs = (
        {
            "times": [
                [2, 1, 1],
                [2, 3, 1],
                [3, 4, 1],
            ],
            "n": 4,
            "k": 2,
            "expected": 2,
        },
        {
            "times": [
                [1, 2, 1],
            ],
            "n": 2,
            "k": 1,
            "expected": 1,
        },
        {
            "times": [
                [1, 2, 1],
            ],
            "n": 2,
            "k": 2,
            "expected": -1,
        },
        {
            "times": [
                [1, 2, 1],
                [2, 3, 2],
                [1, 3, 2]
            ],
            "n": 3,
            "k": 1,
            "expected": 2,
        },
    )

    obj = Solution()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.networkDelayTime(val["times"], val["n"], val["k"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")
    print(f"Passed: {test_passed:3}/{idx + 1}\n")
