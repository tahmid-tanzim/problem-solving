#!/usr/bin/python3
# https://www.algoexpert.io/questions/Same%20BSTs
"""
  An array of integers is said to represent the Binary Search Tree (BST)
  obtained by inserting each integer in the array, from left to right, into the BST.

  Write a function that takes in two arrays of integers and determines whether
  these arrays represent the same BST. Note that you're not allowed to
  construct any BSTs in your code.

  A BST is a Binary Tree that consists only of BST nodes. A node is said to be a
  valid BST node if and only if it satisfies the BST property: its value is
  strictly greater than the values of every node to its left; its value is less
  than or equal to the values of every node to its right; and its children nodes
  are either valid BST nodes themselves or None / null.

Sample Input
arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]

Sample Output
true // both arrays represent the BST below
         10
       /     \
      8      15
    /       /   \
   5      12    94
 /       /     /
2       11    81
"""


def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True
    if len(arrayOne) != len(arrayTwo) or arrayOne[0] != arrayTwo[0]:
        return False

        # Main Logic
    arrayOneLeft = []
    arrayOneRight = []
    arrayTwoLeft = []
    arrayTwoRight = []
    i, n = 1, len(arrayOne)

    while i < n:
        if arrayOne[i] < arrayOne[0]:
            arrayOneLeft.append(arrayOne[i])
        if arrayOne[i] >= arrayOne[0]:
            arrayOneRight.append(arrayOne[i])
        if arrayTwo[i] < arrayTwo[0]:
            arrayTwoLeft.append(arrayTwo[i])
        if arrayTwo[i] >= arrayTwo[0]:
            arrayTwoRight.append(arrayTwo[i])
        i += 1

    return sameBsts(arrayOneLeft, arrayTwoLeft) and sameBsts(arrayOneRight, arrayTwoRight)


if __name__ == "__main__":
    print(sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81]))
