#!/usr/bin/python3
# https://leetcode.com/problems/longest-palindromic-subsequence/


# Top Down, Memoization
# O() time, O() space
class Solution1:
    def _getLCS(self, text1: str, text2: str, m: int, n: int, cache: dict) -> dict:
        if m < 0 or n < 0:
            return dict(length=0, subsequence="")

        key = f"{m}:{n}"
        if key in cache:
            return cache[key]

        if text1[m] == text2[n]:
            UP_LEFT = self._getLCS(text1, text2, m - 1, n - 1, cache)
            length = 1 + UP_LEFT["length"]
            subsequence = UP_LEFT["subsequence"] + text1[m]
            cache[key] = dict(length=length, subsequence=subsequence)
        else:
            UP = self._getLCS(text1, text2, m - 1, n, cache)
            LEFT = self._getLCS(text1, text2, m, n - 1, cache)
            if UP["length"] > LEFT["length"]:
                cache[key] = UP
            else:
                cache[key] = LEFT

        return cache[key]

    def _longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) - 1
        n = len(text2) - 1
        output = self._getLCS(text1, text2, m, n, dict())
        return output['length']
    
    def longestPalindromeSubseq(self, s: str) -> int:
        return self._longestCommonSubsequence(s, s[::-1])


class Solution2:
    def _getLCS(self, text1: str, text2: str, m: int, n: int, cache: dict) -> int:
        if m < 0 or n < 0:
            return 0

        key = f"{m}:{n}"
        if key in cache:
            return cache[key]

        if text1[m] == text2[n]:
            cache[key] = 1 + self._getLCS(text1, text2, m - 1, n - 1, cache)
        else:
            UP = self._getLCS(text1, text2, m - 1, n, cache)
            LEFT = self._getLCS(text1, text2, m, n - 1, cache)
            cache[key] = max(UP, LEFT)

        return cache[key]

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s) - 1
        return self._getLCS(s, s[::-1], n, n, dict())


if __name__ == '__main__':
    obj = Solution2()
    print(obj.longestPalindromeSubseq("bbbab"))
    print(obj.longestPalindromeSubseq("cbbd"))
