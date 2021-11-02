#!/usr/bin/python3
# https://www.algoexpert.io/questions/Largest%20Range
"""
  Write a function that takes in an array of integers and returns an array of
  length 2 representing the largest range of integers contained in that array.

  The first number in the output array should be the first number in the range,
  while the second number should be the last number in the range.

  A range of numbers is defined as a set of numbers that come right after each
  other in the set of real integers. For instance, the output array
  [2, 6] represents the range {2, 3, 4, 5, 6}, which
  is a range of length 5. Note that numbers don't need to be sorted or adjacent
  in the input array in order to form a range.

You can assume that there will only be one largest range.
Sample Input
array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

Sample Output
[0, 7]
"""


# O(n) time, O(n) space
def largestRange(array):
    hashtable = dict()
    largest_range = (array[0], array[0])

    for num in array:
        hashtable[num] = True

    for num in array:
        if not hashtable[num]:
            continue

        hashtable[num] = False

        # Check Left Range
        L = num - 1
        while L in hashtable and hashtable[L]:
            hashtable[L] = False
            L -= 1
        L += 1

        # Check Right Range
        R = num + 1
        while R in hashtable and hashtable[R]:
            hashtable[R] = False
            R += 1
        R -= 1

        if R - L + 1 > largest_range[1] - largest_range[0] + 1:
            largest_range = (L, R)

    return largest_range


if __name__ == '__main__':
    print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
