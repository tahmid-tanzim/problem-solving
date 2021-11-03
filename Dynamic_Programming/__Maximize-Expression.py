#!/usr/bin/python3
# https://www.algoexpert.io/questions/Maximize%20Expression
"""
  Write a function that takes in an array of integers and returns the largest
  possible value for the expression
  array[a] - array[b] + array[c] - array[d], where a,
  b, c, and d are indices of the array
  and a < b < c < d.

  If the input array has fewer than 4 elements, your function
  should return 0.

Sample Input
array = [3, 6, 1, -3, 2, 7]

Sample Output
4
// Choose a = 1, b = 3, c = 4, and d = 5
// -> 6 - (-3) + 2 - 7 = 4
"""


# O(n) time | O(n) space - where n is the length of the array
def maximizeExpression(array):
    return -1


if __name__ == '__main__':
    print(maximizeExpression([3, 6, 1, -3, 2, 7]))
