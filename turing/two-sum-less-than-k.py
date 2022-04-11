#!/usr/bin/python3
# https://leetcode.com/problems/two-sum-less-than-k/
from typing import List

"""
Given an array A of integers and integer K,
return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K.
If no i, j exist satisfying this equation, return -1.

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation:
We can use 34 and 24 to sum 58 which is less than 60.

Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation:
In this case it's not possible to get a pair sum less that 15.

Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
"""


# O(n^2)
def two_sum_less_than_k(arr: List, k: int) -> int:
    result = -1
    i = 0
    n = len(arr)

    while i < n - 1:
        j = i + 1
        while j < n:
            total = arr[i] + arr[j]
            if result < total < k:
                result = total
            j += 1
        i += 1

    return result


if __name__ == "__main__":
    print(two_sum_less_than_k([34, 23, 1, 24, 75, 33, 54, 8], 60))  # 58
    print(two_sum_less_than_k([10, 20, 30], 15))  # -1
