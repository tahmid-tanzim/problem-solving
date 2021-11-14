#!/usr/bin/python3
# https://leetcode.com/problems/shortest-common-supersequence/
"""
supersequence string means - maintain order from start to end but may not be continous

Shortest Supersequence ~> m + n - LCS
"""


# Top Down, Memoization
# O() time, O() space
class Solution1:
    @staticmethod
    def _getLCSString(text1: str, text2: str, m: int, n: int, DP_TABLE) -> dict:
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

        return DP_TABLE[m][n]

    def _longestCommonSubsequence(self, text1: str, text2: str) -> str:
        m = len(text1)
        n = len(text2)
        DP_TABLE = [[dict(length=0, subsequence="") for c in range(n + 1)] for r in range(m + 1)]
        output = self._getLCSString(text1, text2, m, n, DP_TABLE)
        return output['subsequence']

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        superSequence = str()
        subSequence = self._longestCommonSubsequence(str1, str2)
        i, j = 0, 0
        for subSequenceChar in subSequence:
            while i < len(str1) and j < len(str2):
                if str1[i] == subSequenceChar and str2[j] == subSequenceChar:
                    superSequence += subSequenceChar
                    i += 1
                    j += 1
                    break
                elif str1[i] != subSequenceChar and str2[j] == subSequenceChar:
                    superSequence += str1[i]
                    i += 1
                elif str1[i] == subSequenceChar and str2[j] != subSequenceChar:
                    superSequence += str2[j]
                    j += 1
                else:
                    superSequence += str1[i]
                    i += 1
                    superSequence += str2[j]
                    j += 1

        return superSequence + str1[i:] + str2[j:]


# Bottom Up, Tabulation
# O() time, O() space
class Solution2:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        pass


if __name__ == '__main__':
    obj = Solution1()
    print(obj.shortestCommonSupersequence("abac", "cab"))
    print(obj.shortestCommonSupersequence("aaaaaaaa", "aaaaaaaa"))
    print(obj.shortestCommonSupersequence("geek", "eke"))
    print(obj.shortestCommonSupersequence("AGGTAB", "GXTXAYB"))
