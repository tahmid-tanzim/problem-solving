#!/usr/bin/python3
# https://www.algoexpert.io/questions/Longest%20Peak
"""
  Write a function that takes in an array of integers and returns the length of
  the longest peak in the array.

  A peak is defined as adjacent integers in the array that are strictly
  increasing until they reach a tip (the highest value in the peak), at which
  point they become strictly decreasing. At least three integers are required to form a peak.

  For example, the integers 1, 4, 10, 2 form a peak, but the
  integers 4, 0, 10 don't and neither do the integers
  1, 2, 2, 0. Similarly, the integers 1, 2, 3 don't
  form a peak because there aren't any strictly decreasing integers after the 3.

Sample Input
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

Sample Output
6 // 0, 10, 6, 5, -1, -3
"""


# O(n) time, O(1) space
def longestPeak(array):
    all_peaks_index = []
    long_peak = 0

    # Find Peaks
    i = 1
    n = len(array)
    while i < n - 1:
        if array[i] > array[i + 1] and array[i] > array[i - 1]:
            all_peaks_index.append(i)
        i += 1

    for peak_index in all_peaks_index:
        # Traverse Left
        left_index = peak_index - 2
        while left_index >= 0 and array[left_index] < array[left_index + 1]:
            left_index -= 1

        # Traverse Right
        right_index = peak_index + 2
        while right_index < n and array[right_index] < array[right_index - 1]:
            right_index += 1

        if long_peak < (right_index - left_index - 1):
            long_peak = (right_index - left_index - 1)

    return long_peak


if __name__ == '__main__':
    print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
