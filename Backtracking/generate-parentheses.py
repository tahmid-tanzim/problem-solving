#!/usr/bin/python3
# https://leetcode.com/problems/palindrome-partitioning/
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pass


if __name__ == "__main__":
    inputs = (
        {
            "n": 3,
            "expected": [
                "((()))",
                "(()())",
                "(())()",
                "()(())",
                "()()()"
            ],
        },
        {
            "n": 1,
            "expected": ["()"],
        },
    )

    obj = Solution()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.partgenerateParenthesisition(val["n"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")
    print(f"Passed: {test_passed:3}/{idx + 1}\n")
