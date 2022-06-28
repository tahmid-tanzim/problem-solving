#!/usr/bin/python3
# https://leetcode.com/problems/meeting-rooms/
# https://www.lintcode.com/problem/920/
from typing import List

"""
Description
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
"""


class Solution1:
    # Brute Force
    # Time Complexity - O(n log(n))
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


if __name__ == "__main__":
    inputs = (
        {
            "intervals": [[0, 30], [5, 10], [15, 20]],
            "expected": False
        },
        {
            "intervals": [[5, 8], [9, 15]],
            "expected": True
        },
    )

    obj = Solution1()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.canAttendMeetings(val["intervals"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
    print(f"Passed: {test_passed:3}/{idx + 1}\n")
