#!/usr/bin/python3
# https://leetcode.com/problems/sort-array-by-parity/


def sort_array_by_parity(A):
    even, odd = [], []
    for a in A:
        if a % 2 == 0:
            even.append(a)
        else:
            odd.append(a)
    return even + odd


if __name__ == '__main__':
    print(sort_array_by_parity([3, 2, 1, 4]))
