#!/usr/bin/python3
# https://www.algoexpert.io/questions/Right%20Smaller%20Than
"""
  Write a function that takes in an array of integers and returns an array of
  the same length, where each element in the output array corresponds to the
  number of integers in the input array that are to the right of the relevant
  index and that are strictly smaller than the integer at that index.

  In other words, the value at output[i] represents the number of
  integers that are to the right of i and that are strictly smaller
  than input[i].

Sample Input
array = [8, 5, 11, -1, 3, 4, 2]

Sample Output
[5, 4, 4, 0, 1, 1, 0]
// There are 5 integers smaller than 8 to the right of it.
// There are 4 integers smaller than 5 to the right of it.
// There are 4 integers smaller than 11 to the right of it.
// Etc..
"""


# Average case: when the created BST is balanced
# O(nlog(n)) time | O(n) space - where n is the length of the array

# Worst case: when the created BST is like a linked list
# O(n^2) time | O(n) space
def rightSmallerThan(array):
    pass


if __name__ == "__main__":
    print(rightSmallerThan([8, 5, 11, -1, 3, 4, 2]))
