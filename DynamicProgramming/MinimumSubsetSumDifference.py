from typing import List


class MinimumSubsetSumDifference:
    def subset_sum(self, nums: List[int], total: int) -> List[bool]:
        n = len(nums)
        matrix = [[True if c == 0 else False for c in range(total + 1)] for _ in range(n + 1)]

        r = 1
        while r <= n:
            c = 1
            while c <= total:
                if nums[r - 1] <= c:
                    include = matrix[r - 1][c - nums[r - 1]]
                    exclude = matrix[r - 1][c]
                    matrix[r][c] = include or exclude
                else:
                    exclude = matrix[r - 1][c]
                    matrix[r][c] = exclude
                c += 1
            r += 1

        return matrix[-1]  # return last row

    # Method 2: Top Down
    def min_difference(self, nums: List[int]) -> int:
        """
        nums = [1, 2, 7]
        1. Find sum of nums as a the upper boundary i.e. Min diff can't go beyond this range
        _range = 10
        """
        _range = sum(nums)

        """
        2. Consider lower half of the Range to calculate last row of subset sum matrix
        lower_half_subset = {1, 2, 3, 4, 5}
        upper_half_subset = {6, 7, 8, 9, 10}
        Arguments ~> nums = [1, 2, 7], total = 5
        small_subset_vector = [True, True, True, True, False, False]
        """
        small_subset_vector = self.subset_sum(nums, _range // 2)

        """
        3. Find the last index of True 
        Apply formula (Range - 2 * index) to find the minimum difference 
        [
          (0, True), (1, True), (2, True), (3, True), (4, False), (5, False), 
          (6, False), (7, True), (8, True), (9, True), (10, True)
        ] 
        Min Diff is (7 - 3)
        """
        for index, e in reversed(list(enumerate(small_subset_vector))):
            if e:
                return _range - 2 * index
