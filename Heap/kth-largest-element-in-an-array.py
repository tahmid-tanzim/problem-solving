#!/usr/bin/python3
# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List
import heapq
from heap import MinHeap, MaxHeap


# O(n*log(n)) time, O(1) space
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]


# for Heap Time Complexity - O(n*log(k))
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # MIN Heap
        array = []
        for num in nums:
            heapq.heappush(array, num)
            if len(array) > k:
                heapq.heappop(array)
        return array[0]

    def findKthSmallest(self, nums: List[int], k: int) -> int:
        # MAX Heap
        array = []
        for num in nums:
            heapq.heappush(array, -num)
            if len(array) > k:
                heapq.heappop(array)

        return -array[0]


class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        array = []
        minHeap = MinHeap()
        for num in nums:
            minHeap.heappush(array, num)
            if len(array) > k:
                minHeap.heappop(array)
        return minHeap.peek(array)

    def findKthSmallest(self, nums: List[int], k: int) -> int:
        array = []
        maxHeap = MaxHeap()
        for num in nums:
            maxHeap.heappush(array, num)
            if len(array) > k:
                maxHeap.heappop(array)

        return maxHeap.peek(array)


if __name__ == "__main__":
    obj = Solution3()

    print(obj.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(obj.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4

    print(obj.findKthSmallest([3, 2, 1, 5, 6, 4], 2))  # 2
    print(obj.findKthSmallest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 3
