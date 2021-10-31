#!/usr/bin/python3
# https://www.algoexpert.io/questions/Kadane's%20Algorithm
"""
  Write a function that takes in a non-empty array of integers and returns the
  maximum sum that can be obtained by summing up all of the integers in a
  non-empty subarray of the input array. A subarray must only contain adjacent
  numbers (numbers next to each other in the input array).

Sample Input
array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

Sample Output
19 // [1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1]
"""


# Time Complexity - O(n)
# Space Complexity - O(1)
def kadanesAlgorithm(array):
    maximum_total = 0
    current_total = 0

    for item in array:
        if item > current_total + item:
            current_total = item
        else:
            current_total += item

        if maximum_total < current_total:
            maximum_total = current_total

    return maximum_total or -1


if __name__ == "__main__":
    print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
