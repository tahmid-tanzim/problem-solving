#!/usr/bin/python3


def shiftUpMinHeap(array, i):
    while i > 0:
        parent_index = (i - 1) // 2
        if array[i] >= array[parent_index]:
            break
        array[i], array[parent_index] = array[parent_index], array[i]
        i = parent_index


def shiftDownMinHeap(array, i, n):
    left_index = 2 * i + 1
    right_index = 2 * i + 2
    while left_index < n and right_index < n:
        if array[left_index] >= array[right_index] and array[right_index] < array[i]:
            array[i], array[right_index] = array[right_index], array[i]
            i = right_index
        elif array[right_index] > array[left_index] and array[left_index] < array[i]:
            array[i], array[left_index] = array[left_index], array[i]
            i = left_index
        else:
            break
        left_index = 2 * i + 1
        right_index = 2 * i + 2

    if left_index < n and array[left_index] < array[i]:
        array[i], array[left_index] = array[left_index], array[i]


def insertIntoMinHeap(array, val):
    """
    @Time-Complexity O(log(n))
    """
    heap_end_border = len(array)
    array.append(val)
    shiftUpMinHeap(array, heap_end_border)


def deleteFromMinHeap(array, heap_end_border):
    """
    @Time-Complexity O(log(n))
    """
    array[0], array[heap_end_border] = array[heap_end_border], array[0]
    shiftDownMinHeap(array, 0, heap_end_border)
    return array[heap_end_border]


def createMinHeap(array):
    """
    @Time-Complexity O(n)
    """
    n = len(array)
    heap_end_border = n - 1
    while heap_end_border >= 0:
        shiftDownMinHeap(array, heap_end_border, n)
        heap_end_border -= 1


def deleteMinHeap(array):
    """
    @Time-Complexity O(n log(n))
    """
    heap_end_border = len(array) - 1
    while heap_end_border > 0:
        val = deleteFromMinHeap(array, heap_end_border)
        print(f'Deleted Item {val}')
        heap_end_border -= 1


def heapify(array):
    createMinHeap(array)
    deleteMinHeap(array)
    print(f'Min Heap - {array}')


if __name__ == "__main__":
    a = [8, 5, 2, 9, 5, 6, 3]
    heapify(a)
    # Sorted Array  [2, 3, 5, 5, 6, 8, 9]
