#!/usr/bin/python3
# https://leetcode.com/problems/insert-intervals/
from typing import List


class Solution1:
    # Brute Force
    # Time Complexity - O(n)
    # As the intervals already sorted, So we don't need to sort it again
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        result.append(newInterval)
        return result


if __name__ == "__main__":
    inputs = (
        {
            "intervals": [[1, 3], [6, 9]],
            "newInterval": [2, 5],
            "expected": [[1, 5], [6, 9]]
        },
        {
            "intervals": [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            "newInterval": [4, 8],
            "expected": [[1, 2], [3, 10], [12, 16]]
        },
        {
            "intervals": [[1, 3], [5, 7], [8, 12]],
            "newInterval": [4, 6],
            "expected": [[1, 3], [4, 7], [8, 12]]
        },
        {
            "intervals": [[1, 3], [5, 7], [8, 12]],
            "newInterval": [4, 10],
            "expected": [[1, 3], [4, 12]]
        },
        {
            "intervals": [[2, 3], [5, 7]],
            "newInterval": [1, 4],
            "expected": [[1, 4], [5, 7]]
        },
    )

    obj = Solution1()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.insert(val["intervals"], val["newInterval"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
    print(f"Passed: {test_passed:3}/{idx + 1}\n")
