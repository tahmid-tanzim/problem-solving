#!/usr/bin/python3
# https://www.algoexpert.io/questions/Radix%20Sort
"""
Write a function that takes in an array of non-negative integers and returns a
sorted version of that array. Use the Radix Sort algorithm to sort the array.

If you're unfamiliar with Radix Sort, we recommend watching the Conceptual
Overview section of this question's video explanation before starting to code.

Sample Input
array = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]

Sample Output
[2, 12, 65, 87, 234, 345, 654, 3008, 8762]
"""


# O(d * (n + b)) time | O(n + b) space
# where n is the length of the input array,
# d is the max number of digits, and b is the base of the numbering system used
def radixSort(array):
    return []


if __name__ == "__main__":
    print(radixSort([8762, 654, 3008, 345, 87, 65, 234, 12, 2]))
