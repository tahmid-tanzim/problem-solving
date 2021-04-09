#!/usr/bin/python3


def shiftUpMinHeap(array, i):
    while i > 0:
        parent_index = (i - 1) // 2
        if array[i]["num"] >= array[parent_index]["num"]:
            break
        array[i], array[parent_index] = array[parent_index], array[i]
        i = parent_index


def shiftDownMinHeap(array, n):
    i = 0
    left_index = 2 * i + 1
    right_index = 2 * i + 2
    while left_index < n and right_index < n:
        if array[left_index]["num"] >= array[right_index]["num"] and array[right_index]["num"] < array[i]["num"]:
            array[i], array[right_index] = array[right_index], array[i]
            i = right_index
        elif array[right_index]["num"] >= array[left_index]["num"] and array[left_index]["num"] < array[i]["num"]:
            array[i], array[left_index] = array[left_index], array[i]
            i = left_index
        else:
            break
        left_index = 2 * i + 1
        right_index = 2 * i + 2

    if left_index < n and array[left_index]["num"] < array[i]["num"]:
        array[i], array[left_index] = array[left_index], array[i]


def createMinHeap(array):
    """
    @Time-Complexity O(n)
    """
    n = len(array)
    heap_end_border = 1
    while heap_end_border < n:
        shiftUpMinHeap(array, heap_end_border)
        heap_end_border += 1


def deleteFromMinHeap(array):
    """
    @Time-Complexity O(log(n))
    """
    lastIdx = len(array) - 1
    array[0], array[lastIdx] = array[lastIdx], array[0]
    shiftDownMinHeap(array, lastIdx)
    deletedItem = array[lastIdx]
    del array[lastIdx]
    return deletedItem


# O(nlog(k)+k) time | O(n + k) space
def mergeSortedArrays(arrays):
    k = len(arrays)
    sortedList = list()
    minHeap = list()

    for arrayIdx in range(k):
        minHeap.append({
            "arrayIdx": arrayIdx,
            "elementIdx": 0,
            "num": arrays[arrayIdx][0]
        })

    createMinHeap(minHeap)
    while len(minHeap) != 0:
        smallestItem = deleteFromMinHeap(minHeap)
        sortedList.append(smallestItem["num"])
        if smallestItem["elementIdx"] == len(arrays[smallestItem["arrayIdx"]]) - 1:
            continue

        heap_end_border = len(minHeap)
        minHeap.append({
            "arrayIdx": smallestItem["arrayIdx"],
            "elementIdx": smallestItem["elementIdx"] + 1,
            "num": arrays[smallestItem["arrayIdx"]][smallestItem["elementIdx"] + 1]
        })
        shiftUpMinHeap(minHeap, heap_end_border)

    return sortedList


if __name__ == "__main__":
    a = [
        [-95, -74, 1],
        [-28, 28, 95],
        [-89, -78, -67, -66, -25, -22, 2, 38],
        [-86, -35, -25, -13, 41],
        [-85, -77, -21, 72],
        [-55, 4, 84, 98],
        [-75, -73, 22]
    ]
    sortedArray = mergeSortedArrays(a)
    result = [-95, -89, -86, -85, -78, -77, -75, -74, -73,
              -67, -66, -55, -35, -28, -25, -25, -22, -21,
              -13, 1, 2, 4, 22, 28, 38, 41, 72, 84, 95, 98]
    print(sortedArray)
    print(f'Result {sortedArray == result}')
    # [-95, -89, -86, -78, -85, -77, -75, -74, -73, -67, -66, -55, -35, -28, -25, -25, -22, -21, -13, 2, 4, 1, 22, 38, 28, 41, 72, 84, 95, 98]
