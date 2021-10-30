#!/usr/bin/python3
# https://leetcode.com/problems/squares-of-a-sorted-array/
# https://www.algoexpert.io/questions/Sorted%20Squared%20Array
"""
Time complexity of array sort is O(n log(n)).
By using two pointer we can reduce the time complexity to O(n)
"""


def sorted_squares(A):
    output = []
    for a in A:
        output.append(a * a)
    output.sort()
    return output


# Time Complexity - O(n)
# Space Complexity - O(n)
def sortedSquaredArray(array):
    n = len(array)
    front_pointer, back_pointer = 0, n - 1
    squared_array = []

    i = 0
    while i < n:
        if abs(array[front_pointer]) > abs(array[back_pointer]):
            squared_array.insert(0, array[front_pointer] * array[front_pointer])
            front_pointer += 1
        else:
            squared_array.insert(0, array[back_pointer] * array[back_pointer])
            back_pointer -= 1
        i += 1

    return squared_array


if __name__ == '__main__':
    print(sorted_squares([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
    print(sorted_squares([-7, -3, 2, 3, 11]))  # [4, 9, 9, 49, 121]
    print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))  # [1, 4, 9, 25, 36, 64, 81]
