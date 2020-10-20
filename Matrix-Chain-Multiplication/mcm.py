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

    def solve(self, arr: List[int], i: int, j: int) -> int:
        if i >= j:
            return 0

        for k in range(i, j):
            left_arr = self.solve(arr, i, k)
            right_arr = self.solve(arr, k + 1, j)
            temp_ans = left_arr + right_arr + arr[i - 1] * arr[k] * arr[j]

            if temp_ans < self.min_value:
                self.min_value = temp_ans

        return self.min_value


if __name__ == "__main__":
    mcm = MatrixChainMultiplication()
    print(mcm.solve([40, 20, 30, 10, 30], 1, 4))
