#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem


import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def check_magazine(magazine, note):
    magazine_dict = dict()
    for word in magazine:
        if word in magazine_dict:
            magazine_dict[word] += 1
        else:
            magazine_dict[word] = 1

    for word in note:
        if word not in magazine_dict:
            return 'No'
        else:
            if magazine_dict[word] <= 1:
                del magazine_dict[word]
            else:
                magazine_dict[word] -= 1

    return 'Yes'


# def check_magazine(magazine, note):
#     for word in note:
#         try:
#             magazine.remove(word)
#         except ValueError:
#             return 'No'
#     return 'Yes'


def check_magazine(magazine, note):
    for word in note:
        if word in magazine:
            magazine.remove(word)
        else:
            return 'No'
    return 'Yes'


if __name__ == '__main__':
    # mn = input().split()
    # m = int(mn[0])
    # n = int(mn[1])
    #
    # magazine = input().rstrip().split()
    # note = input().rstrip().split()

    # magazine = "give me one grand today night".rstrip().split()
    # note = "give one grand today".rstrip().split()

    # magazine = "two times three is not four".rstrip().split()
    # note = "two times two is four".rstrip().split()

    magazine = "ive got a lovely bunch of coconuts".rstrip().split()
    note = "ive got some coconuts".rstrip().split()

    print(check_magazine(magazine, note))
