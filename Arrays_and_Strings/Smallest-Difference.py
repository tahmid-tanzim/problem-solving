#!/usr/bin/python3
# https://www.algoexpert.io/questions/Smallest%20Difference
"""
  Write a function that takes in two non-empty arrays of integers, finds the
  pair of numbers (one from each array) whose absolute difference is closest to
  zero, and returns an array containing these two numbers, with the number from
  the first array in the first position.

  Note that the absolute difference of two integers is the distance between
  them on the real number line. For example, the absolute difference of -5 and 5
  is 10, and the absolute difference of -5 and -4 is 1.

  You can assume that there will only be one pair of numbers with the smallest
  difference.

Sample Input
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Sample Output
[28, 26]
"""


# Time Complexity - O(nlog(n) + mlog(m))
# Space Complexity - O(1)
def smallestDifference(arrayOne, arrayTwo):
    minDiff = float("inf")
    output = []
    i = 0
    j = 0

    arrayOne.sort()
    arrayTwo.sort()

    while i < len(arrayOne) and j < len(arrayTwo):
        first_val = arrayOne[i]
        second_val = arrayTwo[j]

        if first_val < second_val:
            currentDiff = abs(second_val - first_val)
            i += 1
        elif second_val < first_val:
            currentDiff = abs(first_val - second_val)
            j += 1
        else:
            return [first_val, second_val]

        if currentDiff < minDiff:
            minDiff = currentDiff
            output = [first_val, second_val]

    return output


if __name__ == "__main__":
    print(smallestDifference([- 1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))  # [28, 26]
