#!/usr/bin/python3
# https://www.algoexpert.io/questions/Longest%20Palindromic%20Substring
"""
  Write a function that, given a string, returns its longest palindromic
  substring.

  A palindrome is defined as a string that's written the same forward and
  backward. Note that single-character strings are palindromes.

You can assume that there will only be one longest palindromic substring.
Sample Input
string = "abaxyzzyxf"

Sample Output
"xyzzyx"
"""


# O(n^2) time | O(n) space
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
    print(longestPalindromicSubstring("abaxyzzyxf"))
