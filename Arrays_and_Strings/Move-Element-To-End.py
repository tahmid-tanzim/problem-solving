#!/usr/bin/python3
# https://www.algoexpert.io/questions/Move%20Element%20To%20End
"""
  You're given an array of integers and an integer. Write a function that moves
  all instances of that integer in the array to the end of the array and returns
  the array.

  The function should perform this in place (i.e., it should mutate the input
  array) and doesn't need to maintain the order of the other integers.

Sample Input
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

Sample Output
[1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently
"""


# O(n) time, O(1) space
def moveElementToEnd(array, toMove):
    i = 0
    while i < len(array):
        if array[i] == toMove:
            j = i + 1
            foundOtherValue = False
            while j < len(array):
                if array[j] != toMove:
                    foundOtherValue = True
                    break
                j += 1

            if foundOtherValue:
                # SWAP
                array[i], array[j] = array[j], array[i]
            else:
                break

        i += 1
    return array


if __name__ == '__main__':
    # output is [1, 3, 4, 2, 2, 2, 2, 2]
    print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
