#!/usr/bin/python3

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
