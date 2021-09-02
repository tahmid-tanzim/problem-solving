#!/usr/bin/python3

"""
https://leetcode.com/problems/delete-columns-to-make-sorted/
"""


def min_deletion_size(A):
    counter = 0
    for i in range(len(A[0])):
        prev_char = 0
        for a in A:
            if prev_char > ord(a[i]):
                counter += 1
                break
            else:
                prev_char = ord(a[i])
    return counter


if __name__ == '__main__':
    print(min_deletion_size(["cba", "daf", "ghi"]))
    print(min_deletion_size(["a", "b"]))
    print(min_deletion_size(["zyx", "wvu", "tsr"]))
