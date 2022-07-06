#!/usr/bin/python3
# https://leetcode.com/problems/last-stone-weight/
from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-weight for weight in stones]
        heapq.heapify(stones)

        while len(stones) > 0:
            if len(stones) == 1:
                return -stones[0]
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, x - y)

        return 0


if __name__ == "__main__":
    inputs = (
        {
            "stones": [2, 7, 4, 1, 8, 1],
            "expected": 1
        },
        {
            "stones": [1],
            "expected": 1
        },
    )

    obj = Solution()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.lastStoneWeight(val["stones"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:   {output}\nExpected: {val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
