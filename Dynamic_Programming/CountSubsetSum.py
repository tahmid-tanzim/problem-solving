from typing import List


class CountSubsetSum:
    def __init__(self) -> None:
        self.memoization_table = None

    def set_memoization_table(self, row: int, col: int) -> None:
        # row ~> n & col ~> total
        self.memoization_table = [[None for _ in range(col + 1)] for _ in range(row + 1)]

    # Method 1: Recursion
    def get_subset_sum_count(self, nums: List[int], n: int, total: int) -> int:
        # Base Condition
        if total == 0:
            return 1
        if n == 0:
            return 0

            # Memoization
        if self.memoization_table[n][total] is not None:
            return self.memoization_table[n][total]

        # Choice Diagram
        if nums[n - 1] <= total:
            include = self.get_subset_sum_count(nums, n - 1, total - nums[n - 1])
            exclude = self.get_subset_sum_count(nums, n - 1, total)
            self.memoization_table[n][total] = include + exclude
            return self.memoization_table[n][total]
        else:
            exclude = self.get_subset_sum_count(nums, n - 1, total)
            self.memoization_table[n][total] = exclude
            return self.memoization_table[n][total]

    # Method 2: Top Down
    def count_subset_sum(self, nums: List[int], n: int, total: int) -> int:
        # Initialize with Base Condition
        matrix = [[1 if c == 0 else 0 for c in range(total + 1)] for _ in range(n + 1)]

        r = 1
        while r <= n:
            c = 1
            while c <= total:
                if nums[r - 1] <= c:
                    include = matrix[r - 1][c - nums[r - 1]]
                    exclude = matrix[r - 1][c]
                    matrix[r][c] = include + exclude
                else:
                    exclude = matrix[r - 1][c]
                    matrix[r][c] = exclude
                c += 1
            r += 1

        return matrix[n][total]
