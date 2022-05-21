#!/usr/bin/python3
# https://leetcode.com/problems/find-median-from-data-stream/
import heapq


class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # Make sure every num small is <= every num in large
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size check
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2


if __name__ == "__main__":
    inputs = (
        {
            "actions": ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
            "data": [[], [1], [2], [], [3], []],
            "expected": [None, None, None, 1.5, None, 2.0]
        },
        {
            "A": [5, 9],
            "expected": 4
        },
        {
            "A": [-1000, 1000],
            "expected": 2000
        },
    )

    obj = MedianFinder()
    obj.addNum(1)
    param_2 = obj.findMedian()
    print(param_2)