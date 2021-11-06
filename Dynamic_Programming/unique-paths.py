#!/usr/bin/python3
# https://leetcode.com/problems/unique-paths/


class Solution1:
    # Top Down, Memoization
    def uniquePaths(self, m: int, n: int, dp_memo: dict = {}) -> int:
        # Base Case
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1

        key = f'{m}-{n}'
        if key in dp_memo:
            return dp_memo[key]

        move_down = self.uniquePaths(m - 1, n, dp_memo)
        move_right = self.uniquePaths(m, n - 1, dp_memo)
        dp_memo[key] = move_down + move_right
        return dp_memo[key]


class Solution2:
    # Bottom Up, Tabulation
    def uniquePaths(self, m: int, n: int) -> int:
        # initialize dp_table
        dp_table = []
        for r in range(m):
            row = []
            for c in range(n):
                if r == 0 or c == 0:
                    row.append(1)
                else:
                    row.append(dp_table[r - 1][c] + row[c - 1])
            dp_table.append(row)
        return dp_table[m - 1][n - 1]
    

if __name__ == "__main__":
    obj = Solution1()
    print(obj.uniquePaths(7, 3))
