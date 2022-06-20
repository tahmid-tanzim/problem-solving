#!/usr/bin/python3
# https://leetcode.com/problems/sliding-window-maximum/
import time
import heapq
from typing import List
from collections import deque
from functools import wraps


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # first item in the args, ie `args[0]` is `self`
        print(f'Function {func.__name__} took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


class Solution1:
    # Brute Force
    # Time Complexity - O(k * (n - k))
    def getMaxValue(self, array: List[int], startIdx: int, endIdx: int) -> int:
        currentMax = -10e4
        for i in range(startIdx, endIdx):
            if currentMax < array[i]:
                currentMax = array[i]
        return currentMax

    @timeit
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxValues = []
        for i in range(0, len(nums) - k + 1):
            maxValues.append(self.getMaxValue(nums, i, i + k))
        return maxValues


class Solution2:
    # Max Heap
    # Time Complexity - O(n * log(k))
    @timeit
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        maxHeap = []  # [(val, idx)]
        for endIdx in range(len(nums)):
            while len(maxHeap) > 0 and maxHeap[0][1] <= endIdx - k:
                heapq.heappop(maxHeap)  # discard max value from heap which is out of window
            heapq.heappush(maxHeap, (-1 * nums[endIdx], endIdx,))
            if endIdx >= k - 1:
                results.append(-1 * maxHeap[0][0])
        return results


class Solution3:
    # DEQUE
    # Time Complexity - O(n)
    @timeit
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        Q = deque()
        for i in range(len(nums)):
            if i >= k and nums[i - k] == Q[0]:
                Q.popleft()

            while len(Q) > 0 and Q[-1] < nums[i]:
                Q.pop()

            Q.append(nums[i])
            if i >= k - 1:
                results.append(Q[0])
        return results


def load_inputs():
    import json
    file = open("testcase/sliding-window-maximum.json")
    data = json.load(file)
    file.close()
    return data


if __name__ == "__main__":
    inputs = load_inputs()

    obj = Solution3()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.maxSlidingWindow(val["nums"], val["k"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")
    print(f"Passed: {test_passed:3}/{idx + 1}\n")
