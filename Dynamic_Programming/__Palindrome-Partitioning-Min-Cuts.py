#!/usr/bin/python3
# https://www.algoexpert.io/questions/Palindrome%20Partitioning%20Min%20Cuts
"""
  Given a non-empty string, write a function that returns the minimum number of
  cuts needed to perform on the string such that each remaining substring is a palindrome.

  A palindrome is defined as a string that's written the same forward as
  backward. Note that single-character strings are palindromes.

Sample Input
string = "noonabbad"

Sample Output
2 // noon | abba | d"
"""


# O(n^2) time | O(n^2) space - where n is the length of the input string
def palindromePartitioningMinCuts(string):
    pass


if __name__ == '__main__':
    print(palindromePartitioningMinCuts("noonabbad"))
