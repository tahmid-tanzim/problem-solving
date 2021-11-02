#!/usr/bin/python3
# https://www.algoexpert.io/questions/Quick%20Sort
"""
  Write a function that takes in an array of integers and returns a sorted
  version of that array. Use the Quick Sort algorithm to sort the array.

  If you're unfamiliar with Quick Sort, we recommend watching the Conceptual
  Overview section of this question's video explanation before starting to code.

Sample Input
array = [8, 5, 2, 9, 5, 6, 3]

Sample Output
[2, 3, 5, 5, 6, 8, 9]
"""


# Best: O(nlog(n)) time | O(log(n)) space - where n is the length of the input array
# Average: O(nlog(n)) time | O(log(n)) space - where n is the length of the input array
# Worst: O(n^2) time | O(log(n)) space - where n is the length of the input array
def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return

    pivotIdx = startIdx
    leftIdx, rightIdx = startIdx + 1, endIdx

    while leftIdx <= rightIdx:
        if array[rightIdx] < array[pivotIdx] < array[leftIdx]:
            array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
            leftIdx += 1
            rightIdx -= 1
            continue
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1

    array[pivotIdx], array[rightIdx] = array[rightIdx], array[pivotIdx]

    leftSubarrayIsSmaller = (rightIdx - 1) - startIdx < endIdx - (rightIdx + 1)
    if leftSubarrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)


def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array


if __name__ == '__main__':
    print(quickSort([8, 5, 2, 9, 5, 6, 3]))
