#!/usr/bin/python3
# https://leetcode.com/problems/interval-list-intersections/
from typing import List


class Solution1:
    # Brute Force
    # Time Complexity - O(n)
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        intersectionList = []
        while i < len(firstList) and j < len(secondList):
            firstInterval = firstList[i]
            secondInterval = secondList[j]
            if firstInterval[1] < secondInterval[0]:
                i += 1
            elif secondInterval[1] < firstInterval[0]:
                j += 1
            else:
                newIntersection = [max(firstInterval[0], secondInterval[0]), min(firstInterval[1], secondInterval[1])]
                intersectionList.append(newIntersection)
                if firstInterval[1] < secondInterval[1]:
                    i += 1
                else:
                    j += 1
        return intersectionList


class Solution2:
    # Brute Force
    # Time Complexity - O(n)
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        intersectionList = []
        while i < len(firstList) and j < len(secondList):
            firstInterval = firstList[i]
            secondInterval = secondList[j]

            low, high = max(firstInterval[0], secondInterval[0]), min(firstInterval[1], secondInterval[1])
            if low <= high:
                intersectionList.append([low, high])

            if firstInterval[1] < secondInterval[1]:
                i += 1
            else:
                j += 1

        return intersectionList


if __name__ == "__main__":
    inputs = (
        {
            "firstList": [[0, 2], [5, 10], [13, 23], [24, 25]],
            "secondList": [[1, 5], [8, 12], [15, 24], [25, 26]],
            "expected": [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
        },
        {
            "firstList": [[1, 3], [5, 9]],
            "secondList": [],
            "expected": [],
        },
        {
            "firstList": [[1, 3], [5, 6], [7, 9]],
            "secondList": [[2, 3], [5, 7]],
            "expected": [[2, 3], [5, 6], [7, 7]],
        },
        {
            "firstList": [[1, 3], [5, 7], [9, 12]],
            "secondList": [[5, 10]],
            "expected": [[5, 7], [9, 10]]
        },
    )

    obj = Solution2()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.intervalIntersection(val["firstList"], val["secondList"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
    print(f"Passed: {test_passed:3}/{idx + 1}\n")
