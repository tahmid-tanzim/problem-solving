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


def longestCommonSubsequence(text1: str, text2: str) -> int:
    len_text1 = len(text1)
    len_text2 = len(text2)

    memoization_table = [[None for _ in range(len_text2)] for _ in range(len_text1)]

    def lcs(i, j):
        # Base Case
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


# Top Down, Memoization
# O(m*n) time, O(m*n) space
class Solution1:
    def _lcs(self, text1: str, text2: str, m: int, n: int, cache) -> int:
        if m < 0 or n < 0:
            return 0

        key = f"{m}:{n}"
        if key in cache:
            return cache[key]

        if text1[m] == text2[n]:
            cache[key] = 1 + self._lcs(text1, text2, m - 1, n - 1, cache)
        else:
            cache[key] = max(self._lcs(text1, text2, m - 1, n, cache), self._lcs(text1, text2, m, n - 1, cache))

        return cache[key]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) - 1
        n = len(text2) - 1
        return self._lcs(text1, text2, m, n, dict())

    def _printLCSHelper(self, text1: str, text2: str, m: int, n: int, cache: dict) -> dict:
        if m < 0 or n < 0:
            return dict(length=0, subsequence="")

        key = f"{m}:{n}"
        if key in cache:
            return cache[key]

        if text1[m] == text2[n]:
            UP_LEFT = self._printLCSHelper(text1, text2, m - 1, n - 1, cache)
            length = 1 + UP_LEFT["length"]
            subsequence = UP_LEFT["subsequence"] + text1[m]
            cache[key] = dict(length=length, subsequence=subsequence)
        else:
            UP = self._printLCSHelper(text1, text2, m - 1, n, cache)
            LEFT = self._printLCSHelper(text1, text2, m, n - 1, cache)
            if UP["length"] > LEFT["length"]:
                cache[key] = UP
            else:
                cache[key] = LEFT

        return cache[key]

    def printLongestCommonSubsequence(self, text1: str, text2: str) -> str:
        m = len(text1) - 1
        n = len(text2) - 1
        output = self._printLCSHelper(text1, text2, m, n, dict())
        return f"{output['length']}:{output['subsequence']}"


# Bottom Up, Tabulation
# O(m*n) time, O(m*n) space
class Solution2:
    @staticmethod
    def _lcs(text1: str, text2: str, m: int, n: int, DP_TABLE) -> int:
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if text1[r - 1] == text2[c - 1]:
                    DP_TABLE[r][c] = 1 + DP_TABLE[r - 1][c - 1]
                else:
                    DP_TABLE[r][c] = max(DP_TABLE[r - 1][c], DP_TABLE[r][c - 1])
        # for r in range(m + 1):
        #     print(DP_TABLE[r])
        return DP_TABLE[m][n]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        DP_TABLE = [[0 for c in range(n + 1)] for r in range(m + 1)]
        return self._lcs(text1, text2, m, n, DP_TABLE)

    @staticmethod
    def _printLCSHelper(text1: str, text2: str, m: int, n: int, DP_TABLE) -> dict:
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if text1[r - 1] == text2[c - 1]:
                    UP_LEFT = DP_TABLE[r - 1][c - 1]
                    length = 1 + UP_LEFT["length"]
                    subsequence = UP_LEFT["subsequence"] + text1[r - 1]
                    DP_TABLE[r][c] = dict(length=length, subsequence=subsequence)
                else:
                    UP = DP_TABLE[r - 1][c]
                    LEFT = DP_TABLE[r][c - 1]
                    if UP["length"] > LEFT["length"]:
                        DP_TABLE[r][c] = UP
                    else:
                        DP_TABLE[r][c] = LEFT

        # for r in range(m + 1):
        #     print(DP_TABLE[r])
        return DP_TABLE[m][n]

    def printLongestCommonSubsequence(self, text1: str, text2: str) -> str:
        m = len(text1)
        n = len(text2)
        DP_TABLE = [[dict(length=0, subsequence="") for c in range(n + 1)] for r in range(m + 1)]
        output = self._printLCSHelper(text1, text2, m, n, DP_TABLE)
        return f"{output['length']}:{output['subsequence']}"


# Bottom Up, Tabulation
# O(m*n) time, O(n) space
class Solution3:
    @staticmethod
    def _lcs(text1: str, text2: str, m: int, n: int, DP_ROW_TABLE) -> int:
        for r in range(1, m + 1):
            prevColumnValue = 0
            prevRowArray = DP_ROW_TABLE.copy()
            for c in range(1, n + 1):
                if text1[r - 1] == text2[c - 1]:
                    DP_ROW_TABLE[c] = 1 + prevRowArray[c - 1]
                    prevColumnValue = DP_ROW_TABLE[c]
                else:
                    DP_ROW_TABLE[c] = max(prevRowArray[c], prevColumnValue)
                    prevColumnValue = DP_ROW_TABLE[c]
            # print(DP_ROW_TABLE)
        return DP_ROW_TABLE[n]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        DP_ROW_TABLE = [0 for c in range(n + 1)]
        return self._lcs(text1, text2, m, n, DP_ROW_TABLE)

    @staticmethod
    def _printLCSHelper(text1: str, text2: str, m: int, n: int, DP_ROW_TABLE) -> dict:
        for r in range(1, m + 1):
            prevColumnValue = dict(length=0, subsequence="")
            prevRowArray = DP_ROW_TABLE.copy()
            for c in range(1, n + 1):
                if text1[r - 1] == text2[c - 1]:
                    UP_LEFT = prevRowArray[c - 1]
                    length = 1 + UP_LEFT["length"]
                    subsequence = UP_LEFT["subsequence"] + text1[r - 1]
                    DP_ROW_TABLE[c] = dict(length=length, subsequence=subsequence)
                    prevColumnValue = DP_ROW_TABLE[c]
                else:
                    if prevRowArray[c]["length"] > prevColumnValue["length"]:
                        DP_ROW_TABLE[c] = prevRowArray[c]
                    else:
                        DP_ROW_TABLE[c] = prevColumnValue
                    prevColumnValue = DP_ROW_TABLE[c]
            # print(DP_ROW_TABLE)
        return DP_ROW_TABLE[n]

    def printLongestCommonSubsequence(self, text1: str, text2: str) -> str:
        m = len(text1)
        n = len(text2)
        DP_ROW_TABLE = [dict(length=0, subsequence="") for c in range(n + 1)]
        output = self._printLCSHelper(text1, text2, m, n, DP_ROW_TABLE)
        return f"{output['length']}:{output['subsequence']}"


if __name__ == '__main__':
    # print(longestCommonSubsequence("abcde", "ace"))  # 3
    # print(longestCommonSubsequence("abc", "abc"))  # 3
    # print(longestCommonSubsequence("abc", "def"))  # 0

    # print(lcs_top_down_dp("abcde", "ace"))  # 3
    # print(lcs_top_down_dp("abc", "abc"))  # 3
    # print(lcs_top_down_dp("abc", "def"))  # 0

    # obj = Solution3()
    # print(obj.longestCommonSubsequence("abcde", "ace"))  # 3
    # print(obj.longestCommonSubsequence("abc", "abc"))  # 3
    # print(obj.longestCommonSubsequence("abc", "def"))  # 0
    # print(obj.longestCommonSubsequence("bsbininm", "jmjkbkjkv"))  # 1
    # print(obj.longestCommonSubsequence("abcba", "abcbcba"))  # 5

    obj = Solution3()
    print(obj.printLongestCommonSubsequence("abcde", "ace"))  # 3
    print(obj.printLongestCommonSubsequence("abc", "abc"))  # 3
    print(obj.printLongestCommonSubsequence("abc", "def"))  # 0
    print(obj.printLongestCommonSubsequence("bsbininm", "jmjkbkjkv"))  # 1
    print(obj.printLongestCommonSubsequence("abcba", "abcbcba"))  # 5


