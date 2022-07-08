#!/usr/bin/python3
# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List
import heapq


class Solution1:
    # Merge Sort
    # Time Complexity - O(n * log(n))
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        hashtable = {}
        for n in nums:
            if n in hashtable:
                hashtable[n] += 1
            else:
                hashtable[n] = 1
        return [key for key, value in sorted(hashtable.items(), key=lambda item: item[1])][-K:]


class Solution2:
    # Heap
    # Time Complexity - O(n * log(k))
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        # O(1) time
        if K == len(nums):
            return nums

        hashtable = {}
        # Build Hash Map
        # Time Complexity - O(n)
        for num in nums:
            if num in hashtable:
                hashtable[num] += 1
            else:
                hashtable[num] = 1

        heap = []
        # Time Complexity - O(n)
        for key in hashtable:
            # Time Complexity - O(log(k))
            heapq.heappush(heap, (hashtable[key], key,))
            if len(heap) > K:
                # Time Complexity - O(log(k))
                heapq.heappop(heap)

        # Time Complexity - O(k)
        return [value for frequency, value in heap]


class Solution3:
    # Bucket Sort
    # Time Complexity - O(n)
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        # O(1) time
        n = len(nums)
        if K == n:
            return nums

        frequency = {}
        # Build Hash Map
        # Time Complexity - O(n)
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        group = {}
        for key, value in frequency.items():
            if value not in group:
                group[value] = []
            group[value].append(key)

        arr = []

        for x in range(n, 0, -1):
            if x in group:
                for i in group[x]:
                    arr.append(i)

        return [arr[x] for x in range(0, K)]


if __name__ == '__main__':
    inputs = (
        {
            "nums": [3, 3, 3, 1, 1, 1, 2, 2, 3],
            "K": 2,
            "expected": [1, 3]
        },
        {
            "nums": [1, 1, 1, 2, 2, 3],
            "K": 2,
            "expected": [1, 2]
        },
        {
            "nums": [1],
            "K": 1,
            "expected": [1]
        },
        {
            "nums": [-1, -1],
            "K": 1,
            "expected": [-1]
        },
    )

    obj = Solution2()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.topKFrequent(val["nums"], val["K"])
        output.sort()
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:   {output}\nExpected: {val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
