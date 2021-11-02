#!/usr/bin/python3
# https://www.algoexpert.io/questions/Heap%20Sort
"""
  Write a function that takes in an array of integers and returns a sorted
  version of that array. Use the Heap Sort algorithm to sort the array.

  If you're unfamiliar with Heap Sort, we recommend watching the Conceptual
  Overview section of this question's video explanation before starting to code.

Sample Input
array = [8, 5, 2, 9, 5, 6, 3]

Sample Output
[2, 3, 5, 5, 6, 8, 9]
"""


def shiftUpMaxHeap(array, i):
    while i > 0:
        parent_index = (i - 1) // 2
        if array[i] <= array[parent_index]:
            break
        array[i], array[parent_index] = array[parent_index], array[i]
        i = parent_index


def shiftDownMaxHeap(array, n):
    i = 0
    left_index = 2 * i + 1
    right_index = 2 * i + 2
    while left_index < n and right_index < n:
        if array[left_index] >= array[right_index] and array[left_index] > array[i]:
            array[i], array[left_index] = array[left_index], array[i]
            i = left_index
        elif array[right_index] > array[left_index] and array[right_index] > array[i]:
            array[i], array[right_index] = array[right_index], array[i]
            i = right_index
        else:
            break
        left_index = 2 * i + 1
        right_index = 2 * i + 2

    if left_index < n and array[left_index] > array[i]:
        array[i], array[left_index] = array[left_index], array[i]


def insertIntoMaxHeap(array, val):
    """
    @Time-Complexity O(log(n))
    """
    heap_end_border = len(array)
    array.append(val)
    shiftUpMaxHeap(array, heap_end_border)


def deleteFromMaxHeap(array, heap_end_border):
    """
    @Time-Complexity O(log(n))
    """
    array[0], array[heap_end_border] = array[heap_end_border], array[0]
    shiftDownMaxHeap(array, heap_end_border)
    return array[heap_end_border]


def createMaxHeap(array):
    """
    @Time-Complexity O(n log(n))
    """
    n = len(array)
    heap_end_border = 2
    while heap_end_border < n:
        shiftUpMaxHeap(array, heap_end_border)
        heap_end_border += 1


def deleteMaxHeap(array):
    """
    @Time-Complexity O(n log(n))
    """
    heap_end_border = len(array) - 1
    while heap_end_border > 0:
        val = deleteFromMaxHeap(array, heap_end_border)
        print(f'Deleted Item {val}')
        heap_end_border -= 1


# Best: O(nlog(n)) time | O(1) space - where n is the length of the input array
# Average: O(nlog(n)) time | O(1) space - where n is the length of the input array
# Worst: O(nlog(n)) time | O(1) space - where n is the length of the input array
def heapSort(array):
    createMaxHeap(array)
    deleteMaxHeap(array)
    return array


if __name__ == "__main__":
    print(heapSort([8, 5, 2, 9, 5, 6, 3]))
