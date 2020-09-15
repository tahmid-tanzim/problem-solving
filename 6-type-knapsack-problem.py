#!/usr/local/bin/python3
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# https://www.youtube.com/watch?v=iBnWHZmlIyY
# https://leetcode.com/problems/partition-equal-subset-sum

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
    def is_subset_sum(self, nums: List[int], n: int, total: int) -> bool:
        # Base Condition
        if total == 0:
            return True
        if n == 0:
            return False

        # Memoization
        if self.memoization_table[n][total] is not None:
            return self.memoization_table[n][total]

        # Choice Diagram
        if nums[n - 1] <= total:
            include = self.is_subset_sum(nums, n - 1, total - nums[n - 1])
            exclude = self.is_subset_sum(nums, n - 1, total)
            self.memoization_table[n][total] = include or exclude
            return self.memoization_table[n][total]
        else:
            exclude = self.is_subset_sum(nums, n - 1, total)
            self.memoization_table[n][total] = exclude
            return self.memoization_table[n][total]

    # Method 2: Top Down
    def is_subset_sum_2(self, nums: List[int], n: int, total: int) -> bool:
        # Initialize with Base Condition
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
                    matrix[r][c] = matrix[r - 1][c]
                c += 1
            r += 1
        return matrix[n][total]


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
        print(small_subset_vector)

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


if __name__ == "__main__":
    print('\n:~: Subset Sum :~:\n')
    subset_sum_inputs = (
        {
            'nums': [3, 34, 4, 12, 5, 2],
            'total': 30,
            'output': False,
        },
        {
            'nums': [3, 34, 4, 12, 5, 2],
            'total': 9,
            'output': True
        },
    )

    for i in subset_sum_inputs:
        _n = len(i['nums'])

        ss_rc = SubsetSum()
        ss_rc.set_memoization_table(_n, i['total'])
        ss_rc_o = ss_rc.is_subset_sum(i['nums'], _n, i['total'])
        print(f'Method 1: Recursion.\nExpected Output - {i["output"]}\nOriginal Output - {ss_rc_o}', end='\n\n')

        ss_td = SubsetSum()
        ss_td_o = ss_td.is_subset_sum_2(i['nums'], _n, i['total'])
        print(f'Method 2: Top Down.\nExpected Output - {i["output"]}\nOriginal Output - {ss_td_o}',
              end='\n-----------------------\n')

    print('\n:~: Equal Subset Sum Partition :~:\n')
    equal_subset_sum_partition_inputs = (
        {
            'nums': [1, 5, 11, 5],
            'output': True,
        },
        {
            'nums': [5, 2, 1, 3],
            'output': False
        },
    )

    for i in equal_subset_sum_partition_inputs:
        essp_rc = EqualSubsetSumPartition()
        essp_rc_o = essp_rc.is_eq_partition(i['nums'])
        print(f'Method 1: Recursion.\nExpected Output - {i["output"]}\nOriginal Output - {essp_rc_o}', end='\n\n')

        essp_td = EqualSubsetSumPartition()
        essp_td_o = essp_td.can_partition(i['nums'])
        print(f'Method 2: Top Down.\nExpected Output - {i["output"]}\nOriginal Output - {essp_td_o}',
              end='\n-----------------------\n')

    print('\n:~: Count Subset Sum :~:\n')
    count_subset_sum_inputs = (
        {
            'nums': [10, 2, 5, 3, 8, 6],
            'total': 10,
            'output': 3,
        },
    )

    for i in count_subset_sum_inputs:
        _n = len(i['nums'])

        css_rc = CountSubsetSum()
        css_rc.set_memoization_table(_n, i['total'])
        css_rc_o = css_rc.get_subset_sum_count(i['nums'], _n, i['total'])
        print(f'Method 1: Recursion.\nExpected Output - {i["output"]}\nOriginal Output - {css_rc_o}', end='\n\n')

        css_td = CountSubsetSum()
        css_td_o = css_rc.count_subset_sum(i['nums'], _n, i['total'])
        print(f'Method 2: Top Down.\nExpected Output - {i["output"]}\nOriginal Output - {css_td_o}',
              end='\n-----------------------\n')

    print('\n:~: Minimum Subset Sum Difference :~:\n')
    min_subset_sum_diff_inputs = (
        {
            'nums': [1, 6, 11, 5],
            'output': 1,
        },
        {
            'nums': [1, 2, 7],
            'output': 4,
        },
    )

    for i in min_subset_sum_diff_inputs:
        mssd_td = MinimumSubsetSumDifference()
        mssd_td_o = mssd_td.min_difference(i['nums'])
        print(f'Method 2: Top Down.\nExpected Output - {i["output"]}\nOriginal Output - {mssd_td_o}',
              end='\n-----------------------\n')
