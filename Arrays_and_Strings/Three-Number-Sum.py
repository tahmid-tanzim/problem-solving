#!/usr/bin/python3
# https://www.algoexpert.io/questions/Three%20Number%20Sum
"""
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all triplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these triplets. The numbers in each triplet should be ordered in ascending
  order, and the triplets themselves should be ordered in ascending order with
  respect to the numbers they hold.

  If no three numbers sum up to the target sum, the function should return an
  empty array.

Sample Input
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

Sample Output
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
"""


# O(n^2) time, O(n) space
def threeNumberSum(array, targetSum):
    three_sum = []
    array.sort()
    pointer = 0
    while pointer < len(array) - 2:
        left, right = pointer + 1, len(array) - 1
        while left < right:
            total = array[pointer] + array[left] + array[right]
            if total < targetSum:
                left += 1
            elif total > targetSum:
                right -= 1
            else:
                three_sum.append([array[pointer], array[left], array[right]])
                left += 1
                right -= 1
        pointer += 1
    return three_sum


if __name__ == '__main__':
    # output is [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
    print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
