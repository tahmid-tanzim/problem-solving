#!/usr/bin/python3
# https://www.algoexpert.io/questions/Monotonic%20Array
"""
  Write a function that takes in an array of integers and returns a boolean
  representing whether the array is monotonic.

  An array is said to be monotonic if its elements, from left to right, are
  entirely non-increasing or entirely non-decreasing.

  Non-increasing elements aren't necessarily exclusively decreasing; they simply
  don't increase. Similarly, non-decreasing elements aren't necessarily
  exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.
Sample Input
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

Sample Output
true
"""


# O(n) time, O(1) space
def isMonotonic(array):
    direction: int = 0
    i = 1
    while i < len(array):
        diff = array[i] - array[i - 1]
        if diff < 0:
            direction = -1
            break
        elif diff > 0:
            direction = 1
            break
        i += 1
    i += 1
    while i < len(array):
        diff = array[i] - array[i - 1]
        if (diff < 0 and direction > 0) or (diff > 0 and direction < 0):
            return False
        i += 1
    return True


if __name__ == '__main__':
    print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))  # True
