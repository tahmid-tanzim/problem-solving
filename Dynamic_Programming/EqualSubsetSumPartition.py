from typing import List


class EqualSubsetSumPartition:
    def __init__(self) -> None:
        self.memoization_table = None

    def init_memoization_table(self, row: int, col: int) -> None:
        # row ~> n = 6
        # col ~> total = 30
        # n x total
        self.memoization_table = [[None for _ in range(col + 1)] for _ in range(row + 1)]

    # Method 1: Recursion
    def is_subset_sum(self, nums: List[int], n: int, total: int) -> bool:
        # Base Condition
        if total == 0:
            return True
        if n == 0:
            return False

        # Memoization
        if self.memoization_table[n][total] is not None:
            return self.memoization_table[n][total]

        if nums[n - 1] <= total:
            include = self.is_subset_sum(nums, n - 1, total - nums[n - 1])
            exclude = self.is_subset_sum(nums, n - 1, total)
            self.memoization_table[n][total] = include or exclude
            return self.memoization_table[n][total]
        else:
            exclude = self.is_subset_sum(nums, n - 1, total)
            self.memoization_table[n][total] = exclude
            return self.memoization_table[n][total]

    def is_eq_partition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        n = len(nums)
        total //= 2

        self.init_memoization_table(n, total)
        return self.is_subset_sum(nums, n, total)

    # Method 2: Top Down
    def can_partition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # Base Condition
        if total % 2 != 0:
            return False

        n = len(nums)
        total //= 2

        # Initialize Matrix
        matrix = [[True if c == 0 else False for c in range(total + 1)] for _ in range(n + 1)]

        # Choice Diagram
        r = 1
        while r <= n:
            c = 1
            while c <= total:
                if nums[r - 1] <= c:
                    include = matrix[r - 1][c - nums[r - 1]]
                    exclude = matrix[r - 1][c]
                    matrix[r][c] = include or exclude
                else:
                    matrix[r][c] = matrix[r - 1][c]
                c += 1
            r += 1

        return matrix[n][total]