#!/usr/bin/python3
# https://leetcode.com/problems/minimum-path-sum/
from typing import List

"""
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 
1 -> 3 -> 1
          |
1    5    1
          |
4    2    1
"""


# O(m x n) time, O(m x n) space
class Solution1:
    # Bottom Up, Iterative, Tabulation
    @staticmethod
    def minPathSum(grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # DP_TABLE size - m x n
        DP_TABLE = [[-1 for c in range(n + 1)] for r in range(m + 1)]

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                upVal = DP_TABLE[row - 1][col]
                leftVal = DP_TABLE[row][col - 1]
                if upVal != -1 and leftVal != -1:
                    DP_TABLE[row][col] = min(upVal, leftVal) + grid[row - 1][col - 1]
                elif upVal == -1 and leftVal != -1:
                    DP_TABLE[row][col] = leftVal + grid[row - 1][col - 1]
                elif upVal != -1 and leftVal == -1:
                    DP_TABLE[row][col] = upVal + grid[row - 1][col - 1]
                else:
                    DP_TABLE[row][col] = grid[row - 1][col - 1]

        return DP_TABLE[m][n]


# O(m x n) time, O(n) space
class Solution2:
    # Bottom Up, Iterative, Tabulation
    @staticmethod
    def minPathSum(grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # DP_ROW_TABLE size - n
        DP_ROW_TABLE = [grid[0][0]]
        for col in range(1, n):
            DP_ROW_TABLE.append(DP_ROW_TABLE[col - 1] + grid[0][col])

        for row in range(1, m):
            DP_ROW_TABLE[0] += grid[row][0]
            for col in range(1, n):
                upVal = DP_ROW_TABLE[col]
                leftVal = DP_ROW_TABLE[col - 1]
                DP_ROW_TABLE[col] = min(upVal, leftVal) + grid[row][col]

        return DP_ROW_TABLE[n - 1]


# O(m x n) time, O(1) space
class Solution3:
    # Bottom Up, Iterative, NO Tabulation
    @staticmethod
    def minPathSum(grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for row in range(m):
            for col in range(n):
                if row > 0 and col > 0:
                    grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
                elif row == 0 and col > 0:
                    grid[row][col] += grid[row][col - 1]
                elif row > 0 and col == 0:
                    grid[row][col] += grid[row - 1][col]

        return grid[m - 1][n - 1]


# O(m x n) time, O(m x n) space
class Solution4:
    # Top Down, Recursive, Memoization
    def minPathSumHelper(self, grid: List[List[int]], row: int, col: int, MEMOIZATION) -> int:
        if row == 0 and col == 0:
            MEMOIZATION[row][col] = grid[row][col]

        if MEMOIZATION[row][col] != -1:
            return MEMOIZATION[row][col]

        if row == 0 and col > 0:
            callbackResult = self.minPathSumHelper(grid, row, col - 1, MEMOIZATION)
        elif row > 0 and col == 0:
            callbackResult = self.minPathSumHelper(grid, row - 1, col, MEMOIZATION)
        else:
            upValue = self.minPathSumHelper(grid, row - 1, col, MEMOIZATION)
            leftValue = self.minPathSumHelper(grid, row, col - 1, MEMOIZATION)
            callbackResult = min(upValue, leftValue)

        MEMOIZATION[row][col] = grid[row][col] + callbackResult
        return MEMOIZATION[row][col]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MEMOIZATION = [[-1 for c in range(n)] for r in range(m)]
        self.minPathSumHelper(grid, m - 1, n - 1, MEMOIZATION)
        return MEMOIZATION[m - 1][n - 1]


if __name__ == "__main__":
    obj = Solution4()
    print(obj.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # 7
    print(obj.minPathSum([[1, 2, 3], [4, 5, 6]]))  # 12
    print(obj.minPathSum([[1, 2, 5], [3, 2, 1]]))  # 6
    print(obj.minPathSum([[1, 2], [1, 1]]))  # 3
