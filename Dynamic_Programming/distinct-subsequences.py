#!/usr/bin/python3
# https://leetcode.com/problems/distinct-subsequences/


# Top Down, Memoization
# O(m * n) time, O(m * n) space
class Solution1:
    def getDistinctSubSequences(self, s: str, t: str, i: int, j: int, cache: dict) -> int:
        if j < 0:
            return 1
        if i < 0:
            return 0

        key = f"{i}:{j}"
        if key in cache:
            return cache[key]

        if s[i] == t[j]:
            cache[key] = self.getDistinctSubSequences(s, t, i - 1, j - 1, cache) + self.getDistinctSubSequences(s, t, i - 1, j, cache)
        else:
            cache[key] = self.getDistinctSubSequences(s, t, i - 1, j, cache)
        return cache[key]

    def numDistinct(self, s: str, t: str) -> int:
        return self.getDistinctSubSequences(s, t, len(s) - 1, len(t) - 1, {})


# Bottom Up, Tabulation
# O(m * n) time, O(m * n) space
class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        DP_TABLE = [[1 if c == 0 else 0 for c in range(n + 1)] for r in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    DP_TABLE[i][j] = DP_TABLE[i - 1][j - 1] + DP_TABLE[i - 1][j]
                else:
                    DP_TABLE[i][j] = DP_TABLE[i - 1][j]

        return DP_TABLE[m][n]


if __name__ == "__main__":
    obj = Solution2()
    print(obj.numDistinct("rabbbit", "rabbit"))  # 3
    print(obj.numDistinct("babgbag", "bag"))  # 5
