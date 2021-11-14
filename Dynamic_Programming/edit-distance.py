#!/usr/bin/python3
# https://leetcode.com/problems/edit-distance/


# Bottom Up, Tabulation
# O(m * n) time, O(m * n) space
class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        DP_TABLE = list()
        for r in range(m + 1):
            row = list()
            for c in range(n + 1):
                if r == 0 and c == 0:
                    row.append(0)
                elif r == 0 and c != 0:
                    row.append(c)
                elif r != 0 and c == 0:
                    row.append(r)
                else:
                    if word1[r - 1] == word2[c - 1]:
                        row.append(DP_TABLE[r - 1][c - 1])
                    else:
                        row.append(1 + min(DP_TABLE[r - 1][c - 1], DP_TABLE[r - 1][c], row[c - 1]))
            DP_TABLE.append(row)
        return DP_TABLE[m][n]


# Top Down, Memoization
# O(m * n) time, O(m * n) space
class Solution2:
    def getEditDistance(self, word1: str, word2: str, r: int, c: int, cache: dict) -> int:
        if r == 0 and c == 0:
            return 0
        if r == 0 and c != 0:
            return c
        if r != 0 and c == 0:
            return r

        key = f"{r}:{c}"
        if key in cache:
            return cache[key]

        if word1[r - 1] == word2[c - 1]:
            cache[key] = self.getEditDistance(word1, word2, r - 1, c - 1, cache)
        else:
            UP_LEFT = self.getEditDistance(word1, word2, r - 1, c - 1, cache)
            UP = self.getEditDistance(word1, word2, r - 1, c, cache)
            LEFT = self.getEditDistance(word1, word2, r, c - 1, cache)
            cache[key] = 1 + min(UP_LEFT, UP, LEFT)
        return cache[key]

    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1) - 1
        n = len(word2) - 1
        return self.getEditDistance(word1, word2, m, n, dict())


if __name__ == "__main__":
    obj = Solution2()
    print(obj.minDistance("horse", "ros"))
    print(obj.minDistance("intention", "execution"))
