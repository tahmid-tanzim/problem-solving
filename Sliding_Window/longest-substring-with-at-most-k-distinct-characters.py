#!/usr/bin/python3
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1/
# https://www.lintcode.com/problem/386/

"""
386 · Longest Substring with At Most K Distinct Characters

Given a string S, find the length of the longest substring T that contains at most k distinct characters.

Example 1
Input: S = "eceba" and k = 3
Output: 4
Explanation: T = "eceb"

Example 2
Input: S = "WORLD" and k = 4
Output: 4
Explanation: T = "WORL" or "ORLD"
"""


class Solution1:
    # Brute Force
    # Time Complexity - O(n)
    def longestKSubstr(self, string: str, k: int) -> int:
        startIdx = endIdx = 0
        hashtable = {}
        currentLength = 0
        currentDistinct = 0
        maxLength = -1

        while endIdx < len(string):
            char = string[endIdx]
            if char not in hashtable:
                hashtable[char] = 1
                currentDistinct += 1
            else:
                hashtable[char] += 1
            currentLength += 1

            while currentDistinct > k:  # and startIdx <= endIdx
                hashtable[string[startIdx]] -= 1
                if hashtable[string[startIdx]] == 0:
                    currentDistinct -= 1
                    del hashtable[string[startIdx]]
                currentLength -= 1
                startIdx += 1

            if currentDistinct == k:
                maxLength = max(maxLength, currentLength)
            endIdx += 1

        return maxLength


if __name__ == "__main__":
    inputs = (
        {
            "string": "aabacbebebe",
            "k": 3,
            "expected": 7
        },
        {
            "string": "aaaa",
            "k": 2,
            "expected": -1
        },
        {
            "string": "eceba",
            "k": 3,
            "expected": 4
        },
        {
            "string": "WORLD",
            "k": 4,
            "expected": 4
        },
        {
            "string": "kb",
            "k": 10,
            "expected": -1
        },
    )

    obj = Solution1()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.longestKSubstr(val["string"], val["k"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
    print(f"Passed: {test_passed:3}/{idx + 1}\n")
