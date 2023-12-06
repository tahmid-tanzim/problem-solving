#!/usr/bin/python3
# https://leetcode.com/problems/non-decreasing-subsequences/
from typing import List


def findSubsequences(nums: List[int]) -> List[List[int]]:
    return []


if __name__ == "__main__":
    testcase = (
        {
            "nums": [4, 6, 7, 7],
            "output": [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]
        },
        {
            "nums": [4, 4, 3, 2, 1],
            "output": [[4, 4]]
        },
        {
            "nums": [7],
            "output": []
        },
    )

    for test in testcase:
        result = findSubsequences(test["nums"])
        print(result, result == test["output"])
