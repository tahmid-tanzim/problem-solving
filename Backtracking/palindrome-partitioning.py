#!/usr/bin/python3
# https://leetcode.com/problems/palindrome-partitioning/
from typing import List


class Solution1:
    def partition(self, s: str) -> List[List[str]]:
        pass


if __name__ == "__main__":
    inputs = (
        {
            "s": "aab",
            "expected": [
                ["a", "a", "b"],
                ["aa", "b"]
            ],
        },
        {
            "s": "a",
            "expected": [
                ["a"]
            ],
        },
    )

    obj = Solution1()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.partition(val["s"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")
    print(f"Passed: {test_passed:3}/{idx + 1}\n")
