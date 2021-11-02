#!/usr/bin/python3
# https://www.algoexpert.io/questions/Subarray%20Sort
"""
  Write a function that takes in an array of at least two integers and that
  returns an array of the starting and ending indices of the smallest subarray
  in the input array that needs to be sorted in place in order for the entire
  input array to be sorted (in ascending order).

  If the input array is already sorted, the function should return
  [-1, -1].

Sample Input
array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

Sample Output
[3, 9]
"""


# O(n) time, O(1) space
class Solution1:
    @staticmethod
    def subarraySort(array):
        n = len(array)
        leftIdx = 0
        rightIdx = n - 1
        unsortedSubarrayRange = [-1, -1]

        while leftIdx < rightIdx:
            for i in range(leftIdx + 1, n, 1):
                if array[i] < array[leftIdx]:
                    unsortedSubarrayRange[0] = leftIdx
                    break
            if unsortedSubarrayRange[0] == leftIdx:
                break
            leftIdx += 1

        while rightIdx > leftIdx:
            for i in range(rightIdx, leftIdx - 1, -1):
                if array[i] > array[rightIdx]:
                    unsortedSubarrayRange[1] = rightIdx
                    break
            if unsortedSubarrayRange[1] == rightIdx:
                break
            rightIdx -= 1

        return unsortedSubarrayRange


# O(n) time, O(1) space
class Solution2:
    @staticmethod
    def isOutOfOrder(i, array):
        if i == 0:
            return array[i] > array[i + 1]
        if i == len(array) - 1:
            return array[i] < array[i - 1]
        return array[i] > array[i + 1] or array[i] < array[i - 1]

    def subarraySort(self, array):
        minOutOfOrder = float('inf')
        maxOutOfOrder = float('-inf')
        foundOutOfOrder = False
        i = 0
        n = len(array)

        while i < n:
            if self.isOutOfOrder(i, array):
                minOutOfOrder = min(array[i], minOutOfOrder)
                maxOutOfOrder = max(array[i], maxOutOfOrder)
                foundOutOfOrder = True
            i += 1

        if not foundOutOfOrder:
            return [-1, -1]

        leftIdx = 0
        rightIdx = n - 1

        while minOutOfOrder >= array[leftIdx]:
            leftIdx += 1

        while maxOutOfOrder <= array[rightIdx]:
            rightIdx -= 1

        return [leftIdx, rightIdx]


if __name__ == '__main__':
    obj = Solution1()
    print(f'{obj.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])}')
    obj = Solution2()
    print(f'{obj.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])}')
