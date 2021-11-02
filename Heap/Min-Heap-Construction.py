#!/usr/bin/python3
# https://www.algoexpert.io/questions/Min%20Heap%20Construction
"""
Implement a MinHeap class that supports:

  1. Building a Min Heap from an input array of integers.
  2. Inserting integers in the heap.
  3. Removing the heap's minimum / root value.
  4. Peeking at the heap's minimum / root value.
  5. Sifting integers up and down the heap, which is to be used when inserting
    and removing values.

Note that the heap should be represented in the form of an array.

  If you're unfamiliar with Min Heaps, we recommend watching the
  Conceptual Overview section of this question's video explanation before
  starting to code.

Sample Usage
array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]

// All operations below are performed sequentially.
MinHeap(array): - // instantiate a MinHeap (calls the buildHeap method and populates the heap)
buildHeap(array): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
insert(76): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
peek(): -5
remove(): -5 [2, 7, 6, 24, 8, 8, 24, 391, 76, 56, 12, 24, 48, 41]
peek(): 2
remove(): 2 [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48]
peek(): 6
insert(87): - [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48, 87]
"""


# BuildHeap: O(n) time | O(1) space - where n is the length of the input array
# SiftDown: O(log(n)) time | O(1) space - where n is the length of the heap
# SiftUp: O(log(n)) time | O(1) space - where n is the length of the heap
# Peek: O(1) | O(1)
# Remove: O(log(n)) time | O(1) space - where n is the length of the heap
# Insert: O(log(n)) time | O(1) space - where n is the length of the heap
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in range(firstParentIdx, -1, -1):
            self.siftDown(currentIdx, len(array), array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        leftChildIdx = currentIdx * 2 + 1

        while leftChildIdx < endIdx:
            rightChildIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 < endIdx else -1

            if rightChildIdx != -1 and heap[rightChildIdx] < heap[leftChildIdx]:
                indexToSwap = rightChildIdx
            else:
                indexToSwap = leftChildIdx

            if heap[indexToSwap] < heap[currentIdx]:
                heap[indexToSwap], heap[currentIdx] = heap[currentIdx], heap[indexToSwap]
                currentIdx = indexToSwap
                leftChildIdx = currentIdx * 2 + 1
            else:
                return

    def siftUp(self):
        currentIdx = len(self.heap) - 1
        parentIdx = (currentIdx - 1) // 2

        while currentIdx > 0 and self.heap[currentIdx] < self.heap[parentIdx]:
            self.heap[currentIdx], self.heap[parentIdx] = self.heap[parentIdx], self.heap[currentIdx]
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap), self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp()


if __name__ == '__main__':
    pass
