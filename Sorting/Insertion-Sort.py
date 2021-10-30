#!/usr/bin/python3
# https://www.algoexpert.io/questions/Insertion%20Sort


# Best Time Complexity - O(n), Space Complexity - O(1)
# Avg. & Worst Time Complexity - O(n^2), Space Complexity - O(1)
def insertionSort(array):
    i = 1
    while i < len(array):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
        i += 1
    return array


if __name__ == "__main__":
    print(insertionSort([8, 5, 29, 5, 6, 3]))
