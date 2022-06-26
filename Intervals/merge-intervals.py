#!/usr/bin/python3
# https://leetcode.com/problems/merge-intervals/
from typing import List


class Solution1:
    # Brute Force
    # Time Complexity - O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        mergeList = []
        for start, end in intervals:
            if len(mergeList) == 0 or start > mergeList[-1][1]:
                mergeList.append([start, end])
            else:
                mergeList[-1][1] = max(mergeList[-1][1], end)
        return mergeList


if __name__ == "__main__":
    inputs = (
        {
            "intervals": [[8, 10], [2, 6], [15, 18], [1, 3]],
            "expected": [[1, 6], [8, 10], [15, 18]]
        },
        {
            "intervals": [[1, 4], [4, 5]],
            "expected": [[1, 5]]
        },
        {
            "intervals": [[1, 4], [2, 5], [7, 9]],
            "expected": [[1, 5], [7, 9]]
        },
        {
            "intervals": [[6, 7], [2, 4], [5, 9]],
            "expected": [[2, 4], [5, 9]]
        },
        {
            "intervals": [[1, 4], [2, 6], [3, 5]],
            "expected": [[1, 6]]
        },
        {
            "intervals": [[2, 5], [1, 4], [9, 10], [6, 9]],
            "expected": [[1, 5], [6, 10]]
        },
    )

    obj = Solution1()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.merge(val["intervals"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
    print(f"Passed: {test_passed:3}/{idx + 1}\n")
