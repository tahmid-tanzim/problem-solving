#!/usr/bin/python3
# https://www.algoexpert.io/questions/Bubble%20Sort


# Best Time Complexity - O(n), Space Complexity - O(1)
# Avg. & Worst Time Complexity - O(n^2), Space Complexity - O(1)
def bubbleSort(array):
    isSorted = False
    n = len(array)
    while not isSorted:
        isSorted = True
        i = 0
        while i < n - 1:
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False
            i += 1
        n -= 1
    return array


if __name__ == "__main__":
    print(bubbleSort([8, 5, 29, 5, 6, 3]))
