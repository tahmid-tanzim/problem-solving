#!/usr/bin/python3
# https://leetcode.com/problems/kth-largest-element-in-a-stream/
from typing import List


class KthLargest:
    # MIN Heap
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.size = k

        for num in nums:
            self.add(num)

    def push(self, num: int):
        self.heap.append(num)
        childIdx = len(self.heap) - 1
        while childIdx > 0:
            parentIdx = (childIdx - 1) // 2
            if self.heap[parentIdx] <= self.heap[childIdx]:
                break
            self.heap[parentIdx], self.heap[childIdx] = self.heap[childIdx], self.heap[parentIdx]
            childIdx = parentIdx

    def pop(self) -> int:
        minValue = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]

        parentIdx = 0
        leftChildIdx = 1
        rightChildIdx = 2

        while leftChildIdx < len(self.heap) and rightChildIdx < len(self.heap):
            if self.heap[leftChildIdx] < self.heap[rightChildIdx] and self.heap[leftChildIdx] < self.heap[parentIdx]:
                self.heap[leftChildIdx], self.heap[parentIdx] = self.heap[parentIdx], self.heap[leftChildIdx]
                parentIdx = leftChildIdx
            elif self.heap[leftChildIdx] >= self.heap[rightChildIdx] and self.heap[rightChildIdx] < self.heap[parentIdx]:
                self.heap[rightChildIdx], self.heap[parentIdx] = self.heap[parentIdx], self.heap[rightChildIdx]
                parentIdx = rightChildIdx
            else:
                break
            leftChildIdx = 2 * parentIdx + 1
            rightChildIdx = leftChildIdx + 1

        if leftChildIdx < len(self.heap) and self.heap[leftChildIdx] < self.heap[parentIdx]:
            self.heap[leftChildIdx], self.heap[parentIdx] = self.heap[parentIdx], self.heap[leftChildIdx]

        return minValue

    def add(self, val: int) -> int:
        self.push(val)
        if len(self.heap) > self.size:
            self.pop()
        return self.heap[0]


if __name__ == "__main__":
    obj = KthLargest(3, [4, 5, 8, 2])
    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(9))
    print(obj.add(4))
    # print(obj.heap)
