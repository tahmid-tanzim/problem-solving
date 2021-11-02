#!/usr/bin/python3
# https://www.algoexpert.io/questions/Index%20Equals%20Value
"""
  Write a function that takes in a sorted array of distinct integers and returns
  the first index in the array that is equal to the value at that index. In
  other words, your function should return the minimum index where
  index == array[index].

If there is no such index, your function should return -1.
Sample Input
array = [-5, -3, 0, 3, 4, 5, 9]

Sample Output
3 // 3 == array[3]
"""


# Linear Search
# Time Complexity - O(n)
# Space Complexity - O(1)
class Solution1:
    @staticmethod
    def indexEqualsValue(array):
        n = len(array)
        for i in range(n):
            if i == array[i]:
                return i
        return -1


# Binary Search
# Time Complexity - O(log(n))
# Space Complexity - O(1)
class Solution2:
    @staticmethod
    def binarySearch(array, startIdx, endIdx):
        while startIdx <= endIdx:
            midIdx = startIdx + (endIdx - startIdx) // 2
            if array[midIdx] > midIdx:
                endIdx = midIdx - 1
            elif array[midIdx] < midIdx:
                startIdx = midIdx + 1
            else:
                i = midIdx - 1
                while i >= 0 and i == array[i]:
                    i -= 1
                return i + 1
        return -1

    def indexEqualsValue(self, array):
        return self.binarySearch(array, 0, len(array) - 1)


if __name__ == "__main__":
    obj = Solution1()
    print(obj.indexEqualsValue([-5, -3, 0, 3, 4, 5, 9]))
    obj = Solution2()
    print(obj.indexEqualsValue([-5, -3, 0, 3, 4, 5, 9]))
