#!/usr/bin/python3
# https://leetcode.com/problems/longest-common-subsequence/


def lcs_top_down_dp(text1: str, text2: str) -> int:
    # Initialize with Base Condition
    len_text1 = len(text1)
    len_text2 = len(text2)
    matrix = [[0 for _ in range(len_text2 + 1)] for _ in range(len_text1 + 1)]

    for i in range(1, len_text1 + 1):
        for j in range(1, len_text2 + 1):
            if text1[i - 1] == text2[j - 1]:
                matrix[i][j] = 1 + matrix[i - 1][j - 1]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[len_text1][len_text2]


def longest_common_subsequence(text1: str, text2: str) -> int:
    len_text1 = len(text1)
    len_text2 = len(text2)

    memoization_table = [[None for _ in range(len_text2)] for _ in range(len_text1)]

    def lcs(i, j):
        if i >= len_text1 or j >= len_text2:
            return 0
        elif memoization_table[i][j] is not None:  # Memoization
            return memoization_table[i][j]
        elif text1[i] == text2[j]:
            memoization_table[i][j] = 1 + lcs(i + 1, j + 1)
            return memoization_table[i][j]
        else:
            memoization_table[i][j] = max(lcs(i + 1, j), lcs(i, j + 1))
            return memoization_table[i][j]

    return lcs(0, 0)


if __name__ == '__main__':
    # print(longest_common_subsequence("abcde", "ace"))  # 3
    # print(longest_common_subsequence("abc", "abc"))  # 3
    # print(longest_common_subsequence("abc", "def"))  # 0

    print(lcs_top_down_dp("abcde", "ace"))  # 3
    print(lcs_top_down_dp("abc", "abc"))  # 3
    print(lcs_top_down_dp("abc", "def"))  # 0
