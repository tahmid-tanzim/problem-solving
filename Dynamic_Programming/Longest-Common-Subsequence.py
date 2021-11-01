#!/usr/bin/python3
# https://www.algoexpert.io/questions/Longest%20Common%20Subsequence
"""
  Write a function that takes in two strings and returns their longest common
  subsequence.

  A subsequence of a string is a set of characters that aren't necessarily
  adjacent in the string but that are in the same order as they appear in the
  string. For instance, the characters ["a", "c", "d"] form a
  subsequence of the string "abcd", and so do the characters
  ["b", "d"]. Note that a single character in a string and the
  string itself are both valid subsequences of the string.

  You can assume that there will only be one longest common subsequence.

Sample Input
str1 = "ZXVVYZW"
str2 = "XKYKZPW"

Sample Output
["X", "Y", "Z", "W"]
"""


class Solution1:
    @staticmethod
    def longestCommonSubsequence(str1, str2):
        m = len(str1)
        n = len(str2)
        DP_TABLE = [['' for c in range(n + 1)] for r in range(m + 1)]

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if str1[row - 1] == str2[col - 1]:
                    DP_TABLE[row][col] = DP_TABLE[row - 1][col - 1] + str1[row - 1]
                else:
                    if len(DP_TABLE[row - 1][col]) > len(DP_TABLE[row][col - 1]):
                        DP_TABLE[row][col] = DP_TABLE[row - 1][col]
                    else:
                        DP_TABLE[row][col] = DP_TABLE[row][col - 1]

        return list(DP_TABLE[m][n])


class Solution2:
    @staticmethod
    def longestCommonSubsequence(str1, str2):
        m = len(str1)
        n = len(str2)

        prev_row = ['' for _ in range(n + 1)]
        curr_row = ['']

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if str1[r - 1] == str2[c - 1]:
                    curr_row.append(prev_row[c - 1] + str1[r - 1])
                else:
                    curr_row.append(max(prev_row[c], curr_row[c - 1], key=len))
            prev_row = curr_row
            curr_row = ['']

        return list(prev_row[n])


if __name__ == '__main__':
    obj = Solution1()
    print(obj.longestCommonSubsequence("ZXVVYZW", "XKYKZPW"))
    obj = Solution2()
    print(obj.longestCommonSubsequence("ZXVVYZW", "XKYKZPW"))
