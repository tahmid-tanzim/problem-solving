from typing import List


class NumberOfSubsetByGivenDifference:
    def __init__(self) -> None:
        self.memoization_table = None

    def set_memoization_table(self, row: int, col: int) -> None:
        # row ~> n & col ~> total
        self.memoization_table = [[None for _ in range(col + 1)] for _ in range(row + 1)]

    # Method 1: Recursion
    def count_subset_sum(self, nums: List[int], n: int, total: int):
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
            include = self.count_subset_sum(nums, n - 1, total - nums[n - 1])
            exclude = self.count_subset_sum(nums, n - 1, total)
            self.memoization_table[n][total] = include + exclude
            return self.memoization_table[n][total]
        else:
            exclude = self.count_subset_sum(nums, n - 1, total)
            self.memoization_table[n][total] = exclude
            return self.memoization_table[n][total]

    def get_number_of_subset_from_diff(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        total = (diff + sum(nums)) // 2
        self.set_memoization_table(n, total)
        return self.count_subset_sum(nums, n, total)
