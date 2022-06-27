#!/usr/bin/python3
# https://leetcode.com/problems/non-overlapping-intervals/
from typing import List


class Solution1:
    # Brute Force
    # Time Complexity - O(n)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        count = 0
        for interval in intervals[1:]:
            if interval[0] >= prevEnd:
                # No Overlaps, So increment the prevEnd
                prevEnd = interval[1]
            else:
                # Overlap exist, So we'll keep the lowest 'end' between overlapping interval.
                count += 1
                prevEnd = min(prevEnd, interval[1])
        return count


if __name__ == "__main__":
    inputs = (
        {
            "intervals": [[1, 2], [2, 3], [3, 4], [1, 3]],
            "expected": 1
        },
        {
            "intervals": [[1, 2], [1, 2], [1, 2]],
            "expected": 2
        },
        {
            "intervals": [[1, 2], [2, 3]],
            "expected": 0
        },
        {
            "intervals": [[1, 5], [2, 3]],
            "expected": 1
        },
        {
            "intervals": [[1, 5], [5, 10], [3, 7]],
            "expected": 1
        },
    )

    obj = Solution1()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.eraseOverlapIntervals(val["intervals"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
    print(f"Passed: {test_passed:3}/{idx + 1}\n")
