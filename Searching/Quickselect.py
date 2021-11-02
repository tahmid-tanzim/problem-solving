#!/usr/bin/python3
# https://www.algoexpert.io/questions/Quickselect
"""
  Write a function that takes in an array of distinct integers as well as an
  integer k and that returns the kth smallest integer in that array.

The function should do this in linear time, on average.
Sample Input
array = [8, 5, 2, 9, 7, 6, 3]
k = 3

Sample Output
5
"""


# Best: O(n) time | O(1) space - where n is the length of the input array
# Average: O(n) time | O(1) space - where n is the length of the input array
# Worst: O(n^2) time | O(1) space - where n is the length of the input array
class Solution1:
    @staticmethod
    def sort(array, index):
        while index > 0:
            if array[index - 1] > array[index]:
                array[index - 1], array[index] = array[index], array[index - 1]
            else:
                break
            index -= 1

    def quickselect(self, array, k):
        sorted_array = [None] * k
        pointer = 0

        for val in array:
            if pointer < k:
                sorted_array[pointer] = val
                self.sort(sorted_array, pointer)
                pointer += 1
                continue
            if pointer == k and sorted_array[pointer - 1] > val:
                sorted_array[pointer - 1] = val
                self.sort(sorted_array, pointer - 1)
                continue

        return sorted_array[k - 1]


# Best: O(n) time | O(1) space - where n is the length of the input array
# Average: O(n) time | O(1) space - where n is the length of the input array
# Worst: O(n^2) time | O(1) space - where n is the length of the input array
class Solution2:
    @staticmethod
    def quickSelectHelper(array, startIdx, endIdx, position):
        while True:
            if startIdx > endIdx:
                raise Exception("'startIdx' should not be greater than 'endIdx'")
            pivotIdx = startIdx
            leftIdx = startIdx + 1
            rightIdx = endIdx

            while leftIdx <= rightIdx:
                if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                    array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
                if array[leftIdx] <= array[pivotIdx]:
                    leftIdx += 1
                if array[rightIdx] >= array[pivotIdx]:
                    rightIdx -= 1

            array[pivotIdx], array[rightIdx] = array[rightIdx], array[pivotIdx]
            if rightIdx > position:
                endIdx = rightIdx - 1
            elif rightIdx < position:
                startIdx = rightIdx + 1
            else:
                return array[rightIdx]

    def quickselect(self, array, k):
        position = k - 1
        return self.quickSelectHelper(array, 0, len(array) - 1, position)


if __name__ == '__main__':
    obj = Solution1()
    print(obj.quickselect([8, 5, 2, 9, 7, 6, 3], 3))
    obj = Solution2()
    print(obj.quickselect([8, 5, 2, 9, 7, 6, 3], 3))
