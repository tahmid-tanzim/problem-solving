#!/usr/bin/python3
# https://www.algoexpert.io/questions/Binary%20Search
"""
  Return target index else -1
"""


# Time Complexity - O(log(n))
# Space Complexity - O(1)
def binarySearchIterative(array, target):
    left_index = 0
    right_index = len(array) - 1
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        if target < array[middle_index]:
            right_index = middle_index - 1
        elif target > array[middle_index]:
            left_index = middle_index + 1
        else:
            return middle_index
    return -1


# Time Complexity - O(log(n))
# Space Complexity - O(1)
def binarySearch(array, target, left_index, right_index):
    if left_index > right_index:
        return -1

    middle_index = (left_index + right_index) // 2
    if target < array[middle_index]:
        return binarySearch(array, target, left_index, middle_index - 1)
    elif target > array[middle_index]:
        return binarySearch(array, target, middle_index + 1, right_index)
    else:
        return middle_index


def binarySearchRecursive(array, target):
    return binarySearch(array, target, 0, len(array) - 1)


if __name__ == "__main__":
    pass
