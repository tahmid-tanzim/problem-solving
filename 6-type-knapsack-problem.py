#!/usr/local/bin/python3
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# https://www.youtube.com/watch?v=iBnWHZmlIyY

"""
# Dynamic Programming
# Knapsack variation Problems

1. Subset Sum Problem ~> https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
2. Equal Subset Sum Partition ~> https://www.youtube.com/watch?v=UmMh7xp07kY
3. Count of Subset Sum
4. Minimum Subset Sum Difference
5. Target Sum DP
6. Number of Subset by a given Difference
"""
from typing import List


class SubsetSum:
    def __init__(self) -> None:
        self.memoization_table = None

    def set_memoization_table(self, row: int, col: int) -> None:
        # row ~> n = 6
        # col ~> total = 30
        # n x total
        self.memoization_table = [[None for _ in range(col + 1)] for _ in range(row + 1)]

    # Method 1: Recursion.
    def is_subset_sum(self, arr: List[int], n: int, total: int) -> bool:
        # Base Condition
        if total == 0:
            return True
        if n == 0:
            return False

        # Memoization
        if self.memoization_table[n][total] is not None:
            return self.memoization_table[n][total]

        # Choice Diagram
        if arr[n - 1] <= total:
            include = self.is_subset_sum(arr, n - 1, total - arr[n - 1])
            exclude = self.is_subset_sum(arr, n - 1, total)
            self.memoization_table[n][total] = include or exclude
            return self.memoization_table[n][total]
        else:
            exclude = self.is_subset_sum(arr, n - 1, total)
            self.memoization_table[n][total] = exclude
            return self.memoization_table[n][total]

    # Method 2: Top Down
    def is_subset_sum_2(self, arr: List[int], n: int, total: int) -> bool:
        matrix = [[None for _ in range(total + 1)] for _ in range(n + 1)]

        # Initialize with Base Condition
        r = 0
        while r <= n:
            matrix[r][0] = True
            r += 1

        c = 1
        while c <= total:
            matrix[0][c] = False
            c += 1

        r = 1
        while r <= n:
            c = 1
            while c <= total:
                if arr[r - 1] <= c:
                    include = matrix[r - 1][c - arr[r - 1]]
                    exclude = matrix[r - 1][c]
                    matrix[r][c] = include or exclude
                else:
                    matrix[r][c] = matrix[r - 1][c]
                c += 1
            r += 1
        return matrix[n][total]


class EqualSubsetSumPartition:
    pass


if __name__ == "__main__":
    subset_sum_inputs = (
        {
            'arr': [3, 34, 4, 12, 5, 2],
            'total': 30,
            'n': 6,
            'output': False,
        },
        {
            'arr': [3, 34, 4, 12, 5, 2],
            'total': 9,
            'n': 6,
            'output': True
        },

    )

    for i in subset_sum_inputs:
        ss_rc = SubsetSum()
        ss_rc.set_memoization_table(i['n'], i['total'])
        ss_rc_o = ss_rc.is_subset_sum(i['arr'], i['n'], i['total'])
        print(f'Method 1: Recursion.\nExpected Output - {i["output"]}\nOriginal Output - {ss_rc_o}', end='\n\n')

        ss_td = SubsetSum()
        ss_td_o = ss_td.is_subset_sum_2(i['arr'], i['n'], i['total'])
        print(f'Method 2: Top Down.\nExpected Output - {i["output"]}\nOriginal Output - {ss_td_o}', end='\n-----------------------\n')

