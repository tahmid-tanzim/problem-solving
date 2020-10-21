#!/usr/local/bin/python3


"""
1. MCM
2. Printing MCM
3. Evaluate Expression to TRUE / Boolean Parenthesization
4. Min / Max value of Expression
5. Palindrome Partitioning
6. Scramble String
7. Egg Dropping Problem
"""

from sys import maxsize
from typing import List


class MatrixChainMultiplication:
    def __init__(self):
        self.min_value = maxsize

    def set_memoization_table(self, row: int, col: int) -> None:
        self.memoization_table = [[None for _ in range(col)] for _ in range(row)]

    def solve(self, arr: List[int], i: int, j: int) -> int:
        if i >= j:
            return 0

        if self.memoization_table[i][j] is not None:
            return self.memoization_table[i][j]

        for k in range(i, j):
            left_arr_ans = self.solve(arr, i, k)
            right_arr_ans = self.solve(arr, k + 1, j)
            temp = left_arr_ans + right_arr_ans + arr[i - 1] * arr[k] * arr[j]

            print(f'Temp - {temp} i:{i}, k:{k}, j:{j}')

            if temp < self.min_value:
                self.min_value = temp

        self.memoization_table[i][j] = self.min_value
        return self.min_value


if __name__ == "__main__":
    a = [10, 30, 5, 60]  # [40, 20, 30, 10, 30]
    len_a = len(a)
    mcm = MatrixChainMultiplication()
    mcm.set_memoization_table(len_a, len_a)
    print(mcm.solve(a, 1, len_a - 1))
