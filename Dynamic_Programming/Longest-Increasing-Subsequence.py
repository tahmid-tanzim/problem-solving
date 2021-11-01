#!/usr/bin/python3
# https://leetcode.com/problems/longest-increasing-subsequence/
# https://www.algoexpert.io/questions/Longest%20Increasing%20Subsequence
"""
  Given a non-empty array of integers, write a function that returns the longest
  strictly-increasing subsequence in the array.

  A subsequence of an array is a set of numbers that aren't necessarily adjacent
  in the array but that are in the same order as they appear in the array. For
  instance, the numbers [1, 3, 4] form a subsequence of the array
  [1, 2, 3, 4], and so do the numbers [2, 4]. Note
  that a single number in an array and the array itself are both valid
  subsequences of the array.

  You can assume that there will only be one longest increasing subsequence.

Sample Input
array = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]

Sample Output
[-24, 2, 3, 5, 6, 35]
"""
from typing import List


# Dynamic Programming
# Time - O(n^2)
# Space - O(n)
def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)
    highestLength = 1
    maxLenArray = [1] * n
    for i in range(1, n):
        j = i - 1
        while j >= 0:
            if nums[i] > nums[j] and maxLenArray[i] <= maxLenArray[j]:
                maxLenArray[i] = maxLenArray[j] + 1
                if highestLength < maxLenArray[i]:
                    highestLength = maxLenArray[i]
            j -= 1
    return highestLength


# Brute Force Solution
class Solution1:
    @staticmethod
    def longestIncreasingSubsequence(array):
        subsequences = list()

        for item in array:
            i = len(subsequences) - 1
            while i >= 0:
                if subsequences[i][-1] < item:
                    new_subsequence = subsequences[i].copy()
                    subsequences.append(new_subsequence + [item])
                i -= 1
            subsequences.append([item])

        max_subsequence = {
            "index": 0,
            "length": len(subsequences[0])
        }

        for i in range(1, len(subsequences)):
            length = len(subsequences[i])
            if max_subsequence["length"] < length:
                max_subsequence = {
                    "index": i,
                    "length": length
                }

        return subsequences[max_subsequence["index"]]


# Dynamic Programming
class Solution2:
    @staticmethod
    def longestIncreasingSubsequence(array):
        n = len(array)
        DP_TABLE = [{"prevIdx": 0, "length": 1}]
        highestLength = 1

        for i in range(1, n):
            DP_TABLE.append({"prevIdx": i, "length": 1})
            for j in range(i - 1, -1, -1):
                if array[j] < array[i] and DP_TABLE[j]["length"] + 1 > DP_TABLE[i]["length"]:
                    DP_TABLE[i] = {"prevIdx": j, "length": DP_TABLE[j]["length"] + 1}
            if highestLength < DP_TABLE[i]["length"]:
                highestLength = DP_TABLE[i]["length"]

        subsequences = list()
        i = n - 1
        while i >= 0:
            if DP_TABLE[i]['length'] == highestLength:
                subsequences.append(array[i])
                break
            i -= 1

        currentIdx = i
        while DP_TABLE[currentIdx]['prevIdx'] < currentIdx:
            prevIdx = DP_TABLE[currentIdx]['prevIdx']
            subsequences.insert(0, array[prevIdx])
            currentIdx = prevIdx

        return subsequences


if __name__ == '__main__':
    print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
    print(Solution1.longestIncreasingSubsequence([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]))  # [-24, 2, 3, 5, 6, 35]
    print(Solution2.longestIncreasingSubsequence([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]))  # [-24, 2, 3, 5, 6, 35]
