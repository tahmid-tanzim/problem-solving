#!/usr/bin/python3
# https://www.algoexpert.io/questions/Levenshtein%20Distance
"""
  Write a function that takes in two strings and returns the minimum number of
  edit operations that need to be performed on the first string to obtain the
  second string.

  There are three edit operations: insertion of a character, deletion of a
  character, and substitution of a character for another.
"""


# O(nm) time, O(min(m, n)) space
# n and m is the length of two input string
def levenshteinDistance(str1, str2):
    # Initialize DP Table
    # str1 == row, str2 == col
    n1 = len(str1)
    n2 = len(str2)
    DP_TABLE = []
    for r in range(n1 + 1):
        row = []
        for c in range(n2 + 1):
            if r == 0 and c == 0:
                row.append(0)
            elif r == 0 and c != 0:
                row.append(c)
            elif r != 0 and c == 0:
                row.append(r)
            else:
                min_operation = min(DP_TABLE[r - 1][c - 1], DP_TABLE[r - 1][c], row[c - 1])
                if str1[r - 1] != str2[c - 1]:
                    min_operation += 1
                row.append(min_operation)
        DP_TABLE.append(row)

    # print('DP_TABLE - ', DP_TABLE)
    return DP_TABLE[n1][n2]


if __name__ == '__main__':
    # Output ~> 2
    print(levenshteinDistance("abc", "yabd"))
