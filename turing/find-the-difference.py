#!/usr/bin/python3
# https://leetcode.com/problems/find-the-difference/


def find_the_difference(s, t):
    frequency = dict()
    for s1 in s:
        if s1 in frequency:
            frequency[s1] += 1
        else:
            frequency[s1] = 1

    for s2 in t:
        if s2 in frequency and frequency[s2] > 0:
            frequency[s2] -= 1
        else:
            return s2


if __name__ == "__main__":
    print(find_the_difference("abcd", "cbdea"))  # e
    print(find_the_difference("kxml", "klxml"))  # l
    print(find_the_difference("", "y"))  # y
