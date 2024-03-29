#!/usr/bin/python3
# https://www.algoexpert.io/questions/Disk%20Stacking
"""
  You're given a non-empty array of arrays where each subarray holds three
  integers and represents a disk. These integers denote each disk's width,
  depth, and height, respectively. Your goal is to stack up the disks and to
  maximize the total height of the stack. A disk must have a strictly smaller
  width, depth, and height than any other disk below it.

  Write a function that returns an array of the disks in the final stack,
  starting with the top disk and ending with the bottom disk. Note that you
  can't rotate disks; in other words, the integers in each subarray must
  represent [width, depth, height] at all times.

  You can assume that there will only be one stack with the greatest total
  height.

Sample Input
disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]

Sample Output
[[2, 1, 2], [3, 2, 3], [4, 4, 5]]
// 10 (2 + 3 + 5) is the tallest height we can get by
// stacking disks following the rules laid out above.
"""


def merge(leftSortedArray, rightSortedArray):
    i = 0
    j = 0
    array = []
    while i < len(leftSortedArray) and j < len(rightSortedArray):
        if leftSortedArray[i][2] < rightSortedArray[j][2]:
            array.append(leftSortedArray[i])
            i += 1
        elif leftSortedArray[i][2] > rightSortedArray[j][2]:
            array.append(rightSortedArray[j])
            j += 1
        else:
            if leftSortedArray[i][0] <= rightSortedArray[j][0] and leftSortedArray[i][1] <= rightSortedArray[j][1]:
                array.append(leftSortedArray[i])
                i += 1
            elif leftSortedArray[i][0] >= rightSortedArray[j][0] and leftSortedArray[i][1] >= rightSortedArray[j][1]:
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


# 0 ~> 1 3 1
# 1 ~> 2 1 2 *
# 2 ~> 3 2 3 *
# 3 ~> 2 3 4
# 4 ~> 4 4 5 *
# 5 ~> 2 2 8
def knapsack(disks, n, baseDisk, maxHeight):
    # Base Case
    if n < 0:
        return dict(max_height=maxHeight, valid_disks=baseDisk)

    # Choice Diagram
    if baseDisk[0][0] > disks[n][0] and baseDisk[0][1] > disks[n][1] and baseDisk[0][2] > disks[n][2]:
        print("baseDisk > disks - ", disks[n], baseDisk, maxHeight)
        include = knapsack(disks, n - 1, [disks[n]] + baseDisk, disks[n][2] + maxHeight)
        exclude = knapsack(disks, n - 1, baseDisk, maxHeight)
        # print("baseDisk > disks - ", n, baseDisk, maxHeight)
        return include if include["max_height"] > exclude["max_height"] else exclude
    elif baseDisk[0][0] < disks[n][0] and baseDisk[0][1] < disks[n][1] and baseDisk[0][2] < disks[n][2]:
        print("baseDisk < disks - ", disks[n], baseDisk, maxHeight)
        includeBaseDisk = knapsack(disks, n - 1, baseDisk, maxHeight)
        excludeBaseDisk = knapsack(disks, n - 1, [disks[n]] + baseDisk[1:], maxHeight - baseDisk[0][2] + disks[n][2])
        # print("baseDisk < disks - ", n, baseDisk, maxHeight)
        return includeBaseDisk if includeBaseDisk["max_height"] > excludeBaseDisk["max_height"] else excludeBaseDisk
    else:
        print("baseDisk == disks - ", disks[n], baseDisk, maxHeight)
        includeBaseDisk = knapsack(disks, n - 1, baseDisk, maxHeight)
        includeNDisk = knapsack(disks, n - 1, [disks[n]], disks[n][2])
        return includeBaseDisk if includeBaseDisk["max_height"] > includeNDisk["max_height"] else includeNDisk


# Dynamic Programming
# O(n^2) time | O(n) space - where n is the number of disks
def diskStacking(disks):
    heightSortedDisks = mergeSort(disks)
    for d in heightSortedDisks:
        print(d)
    print("-------------------------------")
    n = len(heightSortedDisks) - 1
    output = knapsack(heightSortedDisks, n - 1, [heightSortedDisks[n]], heightSortedDisks[n][2])
    for d in output["valid_disks"]:
        print(d)


if __name__ == "__main__":
    # diskStacking([
    #     [2, 1, 2],
    #     [3, 2, 3],
    #     [2, 2, 8],
    #     [2, 3, 4],
    #     [1, 3, 1],
    #     [4, 4, 5]
    # ])

    diskStacking([
        [2, 1, 2],
        [3, 2, 3],
        [2, 2, 8],  # *
        [2, 3, 4],
        [1, 2, 1],
        [4, 4, 5],
        [1, 1, 4]  # *
    ])

    # diskStacking([
    #     [3, 3, 4],
    #     [2, 1, 2],
    #     [3, 2, 3],
    #     [2, 2, 8],
    #     [2, 3, 4],
    #     [5, 5, 6],
    #     [1, 2, 1],
    #     [4, 4, 5],
    #     [1, 1, 4],
    #     [2, 2, 3]
    # ])

