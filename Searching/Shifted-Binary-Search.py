#!/usr/bin/python3
# https://www.algoexpert.io/questions/Shifted%20Binary%20Search
"""
  Write a function that takes in a sorted array of distinct integers as well as a target
  integer. The caveat is that the integers in the array have been shifted by
  some amount; in other words, they've been moved to the left or to the right by
  one or more positions. For example, [1, 2, 3, 4] might have
  turned into [3, 4, 1, 2].

  The function should use a variation of the Binary Search algorithm to
  determine if the target integer is contained in the array and should return
  its index if it is, otherwise -1.

  If you're unfamiliar with Binary Search, we recommend watching the Conceptual
  Overview section of the Binary Search question's video explanation before
  starting to code.

Sample Input
array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33

Sample Output
8
"""


# O(log(n)) time | O(log(n)) space
class Solution1:
    def shiftedBinarySearchHelper(self, array, target, left, right):
        if left > right:
            return -1

        middle = (left + right) // 2
        if target == array[middle]:
            return middle

        if array[left] <= array[middle]:
            # left sorted
            if array[left] <= target < array[middle]:
                return self.shiftedBinarySearchHelper(array, target, left, middle - 1)
            else:
                return self.shiftedBinarySearchHelper(array, target, middle + 1, right)
        else:
            # right sorted
            if array[middle] <= target < array[right]:
                return self.shiftedBinarySearchHelper(array, target, middle + 1, right)
            else:
                return self.shiftedBinarySearchHelper(array, target, left, middle - 1)

    def shiftedBinarySearch(self, array, target):
        return self.shiftedBinarySearchHelper(array, target, 0, len(array) - 1)


# O(log(n)) time | O(1) space
class Solution2:
    @staticmethod
    def shiftedBinarySearchHelper(array, target, left, right):
        while left <= right:
            middle = (left + right) // 2
            if target == array[middle]:
                return middle

            if array[left] <= array[middle]:
                # left sorted
                if array[left] <= target < array[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                # right sorted
                if array[middle] <= target < array[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1

    def shiftedBinarySearch(self, array, target):
        return self.shiftedBinarySearchHelper(array, target, 0, len(array) - 1)


if __name__ == '__main__':
    obj = Solution1()
    print(obj.shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 33))
    obj = Solution2()
    print(obj.shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 33))
