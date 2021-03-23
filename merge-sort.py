#!/usr/bin/python3
# https://www.algoexpert.io/questions/Merge%20Sort

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


def mergeSort(array):
    return mergeSortHelper(array, 0, len(array) - 1)


if __name__ == '__main__':
    # print(merge_sort([1, 5, 6, 3, 8, 4, 7, 2, 4]))
    print(mergeSort([38, 27, 43, 3, 9, 82, 10]))
    # print(merge_sort([1, 4, 5, 8, 2, 6, 7, 8, 9]))
    # merge_sort([1, 5, 6, 3, 8, 4, 7])
