#!/usr/bin/python3
# https://www.algoexpert.io/questions/Merge%20Overlapping%20Intervals
"""
  Write a function that takes in a non-empty array of arbitrary intervals,
  merges any overlapping intervals, and returns the new intervals in no
  particular order.

  Each interval interval is an array of two integers, with
  interval[0] as the start of the interval and
  interval[1] as the end of the interval.

  Note that back-to-back intervals aren't considered to be overlapping. For
  example, [1, 5] and [6, 7] aren't overlapping;
  however, [1, 6] and [6, 7] <i>are</i> indeed overlapping.

  Also note that the start of any particular interval will always be less than
  or equal to the end of that interval.

Sample Input
intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]

Sample Output
[[1, 2], [3, 8], [9, 10]]
// Merge the intervals [3, 5], [4, 7], and [6, 8].
// The intervals could be ordered differently.
"""


# O(nog(n)) time, O(n) space
def mergeOverlappingIntervals(intervals):
    i = 0
    n = len(intervals)
    start_time = list()
    end_time = list()

    while i < n:
        start_time.append(intervals[i][0])
        end_time.append(intervals[i][1])
        i += 1

    start_time.sort()
    end_time.sort()
    start_time.append(end_time[-1] + 1)
    merged_intervals = list()
    interval_start = start_time[0]
    i = 0
    while i < n:
        if end_time[i] < start_time[i + 1]:
            merged_intervals.append([interval_start, end_time[i]])
            interval_start = start_time[i + 1]
        i += 1

    return merged_intervals


if __name__ == '__main__':
    # print(f'Answer - {mergeOverlappingIntervals([[6, 6], [1, 5], [2, 4], [1, 3]])}')
    print(f'Answer - {mergeOverlappingIntervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]])}')
