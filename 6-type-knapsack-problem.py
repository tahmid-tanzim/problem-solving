#!/usr/local/bin/python3
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# https://www.youtube.com/watch?v=iBnWHZmlIyY

"""
# Dynamic Programming
# Knapsack variation Problems

1. Subset Sum Problem ~> https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
2. Equal Subset Sum Partition
3. Count of Subset Sum
4. Minimum Subset Sum Difference
5. Target Sum DP
6. Number of Subset by a given Difference
"""

# row ~> n = 6
# col ~> total = 30
memoization_table = list()


# Method 1: Recursion.
def is_subset_sum(arr: list, total: int, n: int) -> bool:
    # Base Condition
    if total == 0:
        return True
    if n == 0:
        return False

    # Memoization
    if memoization_table[n][total] is not None:
        return memoization_table[n][total]

    # Choice Diagram
    if arr[n - 1] <= total:
        include = is_subset_sum(arr, total - arr[n - 1], n - 1)
        exclude = is_subset_sum(arr, total, n - 1)
        memoization_table[n][total] = include or exclude
        return memoization_table[n][total]
    else:
        exclude = is_subset_sum(arr, total, n - 1)
        memoization_table[n][total] = exclude
        return memoization_table[n][total]


# Method 2: To solve the problem in Pseudo-polynomial time use the Dynamic programming.
if __name__ == "__main__":
    subset_sum_inputs = (
        {
            'arr': [3, 34, 4, 12, 5, 2],  # 79
            'total': 30,
            'n': 6,
            'output': False
        },
        {
            'arr': [3, 34, 4, 12, 5, 2],  # 35
            'total': 9,
            'n': 6,
            'output': True
        },

    )

    for i in subset_sum_inputs:
        memoization_table = [[None for _ in range(i['total'] + 1)] for _ in range(i['n'] + 1)]
        o = is_subset_sum(i['arr'], i['total'], i['n'])
        print(f'Expected Output - {i["output"]}\nOriginal Output - {o}', end='\n\n')
