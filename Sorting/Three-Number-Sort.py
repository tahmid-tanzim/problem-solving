#!/usr/bin/python3
# https://www.algoexpert.io/questions/Three%20Number%20Sort
"""
  You're given an array of integers and another array of three distinct
  integers. The first array is guaranteed to only contain integers that are in
  the second array, and the second array represents a desired order for the
  integers in the first array. For example, a second array of
  [x, y, z] represents a desired order of
  [x, x, ..., x, y, y, ..., y, z, z, ..., z] in the first array.

  Write a function that sorts the first array according to the desired order in
  the second array.

  The function should perform this in place (i.e., it should mutate the input
  array), and it shouldn't use any auxiliary space (i.e., it should run with
  constant space: O(1) space).

  Note that the desired order won't necessarily be ascending or descending and
  that the first array won't necessarily contain all three integers found in the
  second array—it might only contain one or two.

Sample Input
array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]

Sample Output
[0, 0, 0, 1, 1, 1, -1, -1]
"""


# Time Complexity - O(n)
# Space Complexity - O(1)
class Solution1:
    @staticmethod
    def threeNumberSort(array, order):
        sorted_array = []
        frequency = [0, 0, 0]
        for val in array:
            try:
                i = order.index(val)
                frequency[i] += 1
            except ValueError:
                frequency[i] = 0

        for i in range(3):
            sorted_array += [order[i]] * frequency[i]

        return sorted_array


# Time Complexity - O(n)
# Space Complexity - O(1)
class Solution2:
    @staticmethod
    def threeNumberSort(array, order):
        firstIdx, secondIdx, thirdIdx = 0, 0, len(array) - 1

        while secondIdx <= thirdIdx:
            value = array[secondIdx]

            if value == order[0]:
                array[firstIdx], array[secondIdx] = array[secondIdx], array[firstIdx]
                firstIdx += 1
                secondIdx += 1

            if value == order[1]:
                secondIdx += 1

            if value == order[2]:
                array[thirdIdx], array[secondIdx] = array[secondIdx], array[thirdIdx]
                thirdIdx -= 1

        return array


if __name__ == '__main__':
    obj = Solution1()
    print(obj.threeNumberSort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))
    obj = Solution2()
    print(obj.threeNumberSort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))
