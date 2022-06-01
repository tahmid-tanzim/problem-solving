#!/usr/bin/python3
# https://leetcode.com/problems/clone-graph/


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        # if neighbors is not None else[]
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None

        hashmap = {
            node.val: Node(node.val)
        }

        # BFS
        queue = [node]
        visited = set()
        visited.add(node.val)

        while len(queue) > 0:
            visitedNode = queue.pop(0)
            visited.add(visitedNode.val)
            # print("Visited Node - ", visitedNode.val)

            if visitedNode.neighbors is None:
                continue

            for neighborNode in visitedNode.neighbors:
                if neighborNode.val not in visited:
                    queue.append(neighborNode)
                    visited.add(neighborNode.val)
                    hashmap[neighborNode.val] = Node(neighborNode.val)

                if hashmap[visitedNode.val].neighbors is None:
                    hashmap[visitedNode.val].neighbors = []
                hashmap[visitedNode.val].neighbors.append(hashmap[neighborNode.val])

        return hashmap[node.val]


if __name__ == "__main__":
   pass