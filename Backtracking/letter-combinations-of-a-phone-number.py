#!/usr/bin/python3
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List
"""
hashtable = {
    "2": ("a", "b", "c"),
    "3": ("d", "e", "f"),
}

("23", i=0, '')

("23", i=1, 'a') ("23", i=1, 'b') ("23", i=1, 'c')

("23", i=2, 'ad') ("23", i=2, 'ae') ("23", i=2, 'af')
("23", i=2, 'bd') ("23", i=2, 'be') ("23", i=2, 'bf')
("23", i=2, 'cd') ("23", i=2, 'ce') ("23", i=2, 'cf')
"""


# Time Complexity O(4^n)
class Solution:
    def __init__(self):
        self.hashtable = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z"),
        }
        self.result: List[str] = []

    def combinationsHelper(self, digits: str, i: int, possibleLetter: str):
        if i == len(digits):
            self.result.append(possibleLetter)
            return

        digitStr = digits[i]
        for letter in self.hashtable[digitStr]:
            self.combinationsHelper(digits, i + 1, possibleLetter + letter)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.result = []
        self.combinationsHelper(digits, 0, "")
        return self.result


if __name__ == "__main__":
    inputs = (
        {
            "digits": "23",
            "expected": ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        },
        {
            "digits": "",
            "expected": [],
        },
        {
            "digits": "2",
            "expected": ["a", "b", "c"],
        },
    )

    obj = Solution()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.letterCombinations(val["digits"])
        if sorted(output) == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")
    print(f"Passed: {test_passed:3}/{idx + 1}\n")
