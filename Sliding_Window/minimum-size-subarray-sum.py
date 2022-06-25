#!/usr/bin/python3
# https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import List


class Solution1:
    # Brute Force
    # Time Complexity - O(n)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = 10e5
        windowSum = startIdx = endIdx = 0

        while endIdx < len(nums):
            windowSum += nums[endIdx]
            while windowSum >= target:
                minLength = min(minLength, endIdx - startIdx + 1)
                windowSum -= nums[startIdx]
                startIdx += 1
            endIdx += 1

        return 0 if minLength == 10e5 else minLength


if __name__ == "__main__":
    inputs = (
        {
            "nums": [2, 3, 1, 2, 4, 3],
            "target": 7,
            "expected": 2
        },
        {
            "nums": [1, 4, 4],
            "target": 4,
            "expected": 1
        },
        {
            "nums": [1, 1, 1, 1, 1, 1, 1, 1],
            "target": 11,
            "expected": 0
        },
        {
            "nums": [2, 1, 5, 2, 3, 2],
            "target": 7,
            "expected": 2
        },
        {
            "nums": [2, 1, 5, 2, 8],
            "target": 7,
            "expected": 1
        },
        {
            "nums": [3, 4, 1, 1, 6],
            "target": 8,
            "expected": 3
        },
    )

    obj = Solution1()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.minSubArrayLen(val["target"], val["nums"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
    print(f"Passed: {test_passed:3}/{idx + 1}\n")
