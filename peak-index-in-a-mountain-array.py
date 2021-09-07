#!/usr/bin/python3
# https://leetcode.com/problems/peak-index-in-a-mountain-array/


def peak_index_in_mountain_array(A):
    i, mx = 0, -1
    while i < len(A):
        if A[i] >= mx:
            mx = A[i]
        else:
            return i - 1
        i += 1


if __name__ == '__main__':
    print(peak_index_in_mountain_array([0, 1, 0]))
