#!/usr/bin/python3
# https://www.algoexpert.io/questions/Search%20For%20Range
"""
  Write a function that takes in a sorted array of integers as well as a target
  integer. The function should use a variation of the Binary Search algorithm to
  find a range of indices in between which the target number is contained in the
  array and should return this range in the form of an array.

  The first number in the output array should represent the first index at which
  the target number is located, while the second number should represent the
  last index at which the target number is located. The function should return
  [-1, -1] if the integer isn't contained in the array.

  If you're unfamiliar with Binary Search, we recommend watching the Conceptual
  Overview section of the Binary Search question's video explanation before
  starting to code.

Sample Input
array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
target = 45

Sample Output
[4, 9]
"""


# Linear
# O(n) time
class Solution1:
    @staticmethod
    def searchForRange(array, target):
        index_range = [-1, -1]
        for i in range(len(array)):
            if array[i] > target:
                break
            if array[i] == target and index_range[0] == -1:
                index_range = [i, i]
            if array[i] == target and index_range[0] != -1:
                index_range[1] = i
        return index_range


# Time Complexity - O(log(n))
# Space Complexity - O(1)
class Solution2:
    def searchForRangeHelper(self, array, left, right, target, finalRange, shouldGoLeft):
        if left > right:
            return

        mid = left + (right - left) // 2
        if target > array[mid]:
            self.searchForRangeHelper(array, mid + 1, right, target, finalRange, shouldGoLeft)
        elif target < array[mid]:
            self.searchForRangeHelper(array, left, mid - 1, target, finalRange, shouldGoLeft)
        else:
            if shouldGoLeft:
                if mid == 0 or array[mid - 1] != target:
                    finalRange[0] = mid
                else:
                    self.searchForRangeHelper(array, left, mid - 1, target, finalRange, shouldGoLeft)
            else:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    finalRange[1] = mid
                else:
                    self.searchForRangeHelper(array, mid + 1, right, target, finalRange, shouldGoLeft)

    def searchForRange(self, array, target):
        finalRange = [-1, -1]
        self.searchForRangeHelper(array, 0, len(array) - 1, target, finalRange, True)
        self.searchForRangeHelper(array, 0, len(array) - 1, target, finalRange, False)
        return finalRange


if __name__ == '__main__':
    obj = Solution1()
    print(obj.searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45))
    obj = Solution2()
    print(obj.searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45))
