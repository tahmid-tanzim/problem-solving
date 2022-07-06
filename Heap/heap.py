#!/usr/bin/python3
from typing import List


class MinHeap:
    def heappop(self, heap: List[int]) -> int:
        """
            @TimeComplexity: O(log(n))
            @Description: Pop and return the smallest item from the heap, maintaining the heap invariant.
            If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].     
        """
        try:
            minValue = heap[0]

            # Put the last leaf in root node.
            heap[0] = heap[-1]
            del heap[-1]

            # Shift down the root node at its correct position
            parentIdx = 0
            leftChildIdx = 2 * parentIdx + 1
            rightChildIdx = 2 * parentIdx + 2

            while leftChildIdx < len(heap) and rightChildIdx < len(heap):
                if heap[leftChildIdx] < heap[rightChildIdx] and heap[parentIdx] > heap[leftChildIdx]:
                    heap[parentIdx], heap[leftChildIdx] = heap[leftChildIdx], heap[parentIdx]
                    parentIdx = leftChildIdx
                elif heap[leftChildIdx] >= heap[rightChildIdx] and heap[parentIdx] > heap[rightChildIdx]:
                    heap[parentIdx], heap[rightChildIdx] = heap[rightChildIdx], heap[parentIdx]
                    parentIdx = rightChildIdx
                else:
                    break
                leftChildIdx = 2 * parentIdx + 1
                rightChildIdx = 2 * parentIdx + 2

            # If while loop break due to rightChildIdx then check if leftChildIdx need swap
            if leftChildIdx < len(heap) and heap[parentIdx] > heap[leftChildIdx]:
                heap[parentIdx], heap[leftChildIdx] = heap[leftChildIdx], heap[parentIdx]

            return minValue

        except IndexError:
            print("Heap is empty")

    def heappush(self, heap: List[int], item: int):
        """
            @TimeComplexity: O(log(n))
            @Description: Push the value item onto the heap, Then shift up the value with its parent
        """
        heap.append(item)
        childIdx = len(heap) - 1
        while childIdx > 0:
            parentIdx = (childIdx - 1) // 2
            if heap[childIdx] >= heap[parentIdx]:  # Break is child is not smaller than parent
                break
            heap[childIdx], heap[parentIdx] = heap[parentIdx], heap[childIdx]
            childIdx = parentIdx

    def heapify(self, array: List[int]):
        """
        @TimeComplexity: O(n)
        @Description: Transform array into a heap, in-place, in linear time.    
        """
        # Heapify will start from the parent of last child. 
        n = len(array)
        parentIdx = (n - 1) // 2
        while parentIdx >= 0:
            leftChildIdx = 2 * parentIdx + 1
            rightChildIdx = 2 * parentIdx + 2

            # Check If right child exist
            if rightChildIdx < n:
                if array[leftChildIdx] < array[rightChildIdx] and array[parentIdx] > array[leftChildIdx]:
                    array[parentIdx], array[leftChildIdx] = array[leftChildIdx], array[parentIdx]
                elif array[leftChildIdx] >= array[rightChildIdx] and array[parentIdx] > array[rightChildIdx]:
                    array[parentIdx], array[rightChildIdx] = array[rightChildIdx], array[parentIdx]

            # Check If right child NOT exist
            elif rightChildIdx == n and array[parentIdx] > array[leftChildIdx]:
                array[parentIdx], array[leftChildIdx] = array[leftChildIdx], array[parentIdx]

            parentIdx -= 1

    def peek(self, heap: List[int]) -> int:
        try:
            return heap[0]
        except IndexError:
            print("Heap is empty")


class MaxHeap:
    def heappop(self, heap: List[int]) -> int:
        """
            @TimeComplexity: O(log(n))
            @Description: Pop and return the largest item from the heap, maintaining the heap invariant.
            If the heap is empty, IndexError is raised. To access the largest item without popping it, use heap[0].
        """
        try:
            maxValue = heap[0]

            # Put the last leaf in root node.
            heap[0] = heap[-1]
            del heap[-1]

            # Shift down the root node at its correct position
            parentIdx = 0
            leftChildIdx = 2 * parentIdx + 1
            rightChildIdx = 2 * parentIdx + 2

            while leftChildIdx < len(heap) and rightChildIdx < len(heap):
                if heap[leftChildIdx] > heap[rightChildIdx] and heap[parentIdx] < heap[leftChildIdx]:
                    heap[parentIdx], heap[leftChildIdx] = heap[leftChildIdx], heap[parentIdx]
                    parentIdx = leftChildIdx
                elif heap[leftChildIdx] <= heap[rightChildIdx] and heap[parentIdx] < heap[rightChildIdx]:
                    heap[parentIdx], heap[rightChildIdx] = heap[rightChildIdx], heap[parentIdx]
                    parentIdx = rightChildIdx
                else:
                    break
                leftChildIdx = 2 * parentIdx + 1
                rightChildIdx = 2 * parentIdx + 2

            # If while loop break due to rightChildIdx then check if leftChildIdx need swap
            if leftChildIdx < len(heap) and heap[parentIdx] < heap[leftChildIdx]:
                heap[parentIdx], heap[leftChildIdx] = heap[leftChildIdx], heap[parentIdx]

            return maxValue

        except IndexError:
            print("Heap is empty")

    def heappush(self, heap: List[int], item: int):
        """
            @TimeComplexity: O(log(n))
            @Description: Push the value item onto the heap, Then shift up the value with its parent
        """
        heap.append(item)
        childIdx = len(heap) - 1
        while childIdx > 0:
            parentIdx = (childIdx - 1) // 2
            if heap[childIdx] <= heap[parentIdx]:  # Break is child is not smaller than parent
                break
            heap[childIdx], heap[parentIdx] = heap[parentIdx], heap[childIdx]
            childIdx = parentIdx

    def heapify(self, array: List[int]):
        """
        @TimeComplexity: O(n)
        @Description: Transform array into a heap, in-place, in linear time.
        """
        # Heapify will start from the parent of last child.
        n = len(array)
        parentIdx = (n - 1) // 2
        while parentIdx >= 0:
            leftChildIdx = 2 * parentIdx + 1
            rightChildIdx = 2 * parentIdx + 2

            # Check If right child exist
            if rightChildIdx < n:
                if array[leftChildIdx] > array[rightChildIdx] and array[parentIdx] < array[leftChildIdx]:
                    array[parentIdx], array[leftChildIdx] = array[leftChildIdx], array[parentIdx]
                elif array[leftChildIdx] <= array[rightChildIdx] and array[parentIdx] < array[rightChildIdx]:
                    array[parentIdx], array[rightChildIdx] = array[rightChildIdx], array[parentIdx]

            # Check If right child NOT exist
            elif rightChildIdx == n and array[parentIdx] < array[leftChildIdx]:
                array[parentIdx], array[leftChildIdx] = array[leftChildIdx], array[parentIdx]

            parentIdx -= 1

    def peek(self, heap: List[int]) -> int:
        try:
            return heap[0]
        except IndexError:
            print("Heap is empty")


def testMinHeap():
    minHeapQ = MinHeap()

    print("""
        #############################################################
        #                MIN Heap Push & Pop - O(log(n))            #
        #############################################################
        """)
    priorityQueue: List[int] = []
    randomNumbers = (70, 30, 90, 50, 10, 60, 10, 20, 40, 30,)
    # Heap Push - O(log(n))
    for num in randomNumbers:
        minHeapQ.heappush(priorityQueue, num)
    print(priorityQueue)

    # Heap Pop - O(log(n))
    for _ in range(10):
        print(minHeapQ.heappop(priorityQueue))

    print("""
        #############################################################
        #                     MIN Heapify - O(n)                    #
        #############################################################
        """)
    numbers: List[int] = [70, 30, 90, 50, 10, 60, 10, 20, 40, 30]
    minHeapQ.heapify(numbers)
    minHeapQ.heappush(numbers, 5)
    print(numbers)
    for _ in range(12):
        print(minHeapQ.heappop(numbers))


def testMaxHeap():
    maxHeapQ = MaxHeap()

    print("""
        #############################################################
        #                MAX Heap Push & Pop - O(log(n))            #
        #############################################################
        """)
    priorityQueue: List[int] = []
    randomNumbers = (70, 30, 90, 50, 10, 60, 10, 20, 40, 30,)
    # Heap Push - O(log(n))
    for num in randomNumbers:
        maxHeapQ.heappush(priorityQueue, num)
    print(priorityQueue)

    # Heap Pop - O(log(n))
    for _ in range(10):
        print(maxHeapQ.heappop(priorityQueue))

    print("""
        #############################################################
        #                     MAX Heapify - O(n)                    #
        #############################################################
        """)
    numbers: List[int] = [70, 30, 90, 50, 10, 60, 10, 20, 40, 30]
    maxHeapQ.heapify(numbers)
    maxHeapQ.heappush(numbers, 95)
    print(numbers)
    for _ in range(12):
        print(maxHeapQ.heappop(numbers))


if __name__ == "__main__":
    testMinHeap()
    testMaxHeap()
