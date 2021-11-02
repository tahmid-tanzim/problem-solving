#!/usr/bin/python3
# https://www.algoexpert.io/questions/Merge%20Sort
"""
  Write a function that takes in an array of integers and returns a sorted
  version of that array. Use the Merge Sort algorithm to sort the array.

  If you're unfamiliar with Merge Sort, we recommend watching the Conceptual
  Overview section of this question's video explanation before starting to code.

Sample Input
array = [8, 5, 2, 9, 5, 6, 3]

Sample Output
[2, 3, 5, 5, 6, 8, 9]
"""


def merge(leftSortedArray, rightSortedArray):
    i = 0
    j = 0
    array = []
    while i < len(leftSortedArray) and j < len(rightSortedArray):
        if leftSortedArray[i] < rightSortedArray[j]:
            array.append(leftSortedArray[i])
            i += 1
        elif leftSortedArray[i] > rightSortedArray[j]:
            array.append(rightSortedArray[j])
            j += 1
        else:
            array.append(leftSortedArray[i])
            i += 1
            array.append(rightSortedArray[j])
            j += 1

    while i < len(leftSortedArray):
        array.append(leftSortedArray[i])
        i += 1

    while j < len(rightSortedArray):
        array.append(rightSortedArray[j])
        j += 1

    return array


def mergeSortHelper(array, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return []

    if leftIdx == rightIdx:
        return [array[leftIdx]]

    middleIdx = (leftIdx + rightIdx) // 2
    leftSortedArray = mergeSortHelper(array, leftIdx, middleIdx)
    rightSortedArray = mergeSortHelper(array, middleIdx + 1, rightIdx)
    return merge(leftSortedArray, rightSortedArray)


# Best: O(nlog(n)) time | O(n) space - where n is the length of the input array
# Average: O(nlog(n)) time | O(n) space - where n is the length of the input array
# Worst: O(nlog(n)) time | O(n) space - where n is the length of the input array
def mergeSort(array):
    return mergeSortHelper(array, 0, len(array) - 1)


if __name__ == '__main__':
    # print(merge_sort([1, 5, 6, 3, 8, 4, 7, 2, 4]))
    print(mergeSort([38, 27, 43, 3, 9, 82, 10]))
    # print(merge_sort([1, 4, 5, 8, 2, 6, 7, 8, 9]))
    # merge_sort([1, 5, 6, 3, 8, 4, 7])
