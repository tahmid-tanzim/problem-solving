#!/usr/bin/python3
"""
https://www.algoexpert.io/questions/Longest%20Palindromic%20Substring
"""


def longestPalindromicSubstring(string):
    palindromicSubstring = ''
    n = len(string)
    i = 0
    leftPointer = 0
    rightPointer = 0
    while i < n:
        # Check if palindrome string length is ODD
        while (leftPointer >= 0 and rightPointer < n) and string[leftPointer] == string[rightPointer]:
            leftPointer -= 1
            rightPointer += 1
        if len(palindromicSubstring) < (rightPointer - leftPointer - 1):
            palindromicSubstring = string[leftPointer + 1:rightPointer]

        # Check if palindrome string length is EVEN
        leftPointer = i - 1
        rightPointer = i
        while (leftPointer >= 0 and rightPointer < n) and string[leftPointer] == string[rightPointer]:
            leftPointer -= 1
            rightPointer += 1
        if len(palindromicSubstring) < (rightPointer - leftPointer - 1):
            palindromicSubstring = string[leftPointer + 1:rightPointer]

        i += 1
        leftPointer = i
        rightPointer = i

    return palindromicSubstring


if __name__ == '__main__':
    print(longestPalindromicSubstring('a'))
