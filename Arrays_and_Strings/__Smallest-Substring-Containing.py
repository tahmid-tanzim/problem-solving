#!/usr/bin/python3
# https://www.algoexpert.io/questions/Smallest%20Substring%20Containing
"""
  You're given two non-empty strings: a big string and a small string. Write a
  function that returns the smallest substring in the big string that contains
  all of the small string's characters.

  Note that:
    1. The substring can contain other characters not found in the small string.
    2. The characters in the substring don't have to be in the same order as they
    appear in the small string.
    3. If the small string has duplicate characters, the substring has to contain
    those duplicate characters (it can also contain more, but not fewer).

  You can assume that there will only be one relevant smallest substring.

Sample Input
bigString = "abcd$ef$axb$c$"
smallString = "$$abf"

Sample Output
"f$axb$"
"""


# O(b + s) time | O(b + s) space
# where b is the length of the big input string and s is the length of the small input string
def smallestSubstringContaining(bigString, smallString):
    pass


if __name__ == '__main__':
    print(smallestSubstringContaining("abcd$ef$axb$c$", "$$abf"))
