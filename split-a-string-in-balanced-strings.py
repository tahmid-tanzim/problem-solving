#!/usr/bin/python3

"""
https://leetcode.com/problems/split-a-string-in-balanced-strings/
"""


def balanced_string_split(s):
    counter = {'L': 0, 'R': 0, 'MAX': 0}
    for char in s:
        counter[char] += 1
        if counter['L'] == counter['R']:
            counter = {'L': 0, 'R': 0, 'MAX': counter['MAX'] + 1}
    return counter['MAX']


if __name__ == '__main__':
    print(balanced_string_split("RLRRLLRLRL"))
    print(balanced_string_split("RLLLLRRRLR"))
    print(balanced_string_split("LLLLRRRR"))
    print(balanced_string_split("RLRRRLLRLL"))
