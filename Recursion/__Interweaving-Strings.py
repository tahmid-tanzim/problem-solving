#!/usr/bin/python3
# https://www.algoexpert.io/questions/Interweaving%20Strings
"""
  Write a function that takes in three strings and returns a boolean
  representing whether the third string can be formed by interweaving the first two strings.

  To interweave strings means to merge them by alternating their letters without
  any specific pattern. For instance, the strings "abc" and
  "123" can be interwoven as "a1b2c3", as "abc123", and as "ab1c23" (this list is nonexhaustive).

  Letters within a string must maintain their relative ordering in the interwoven string.

Sample Input
one = "algoexpert"
two = "your-dream-job"
three = "your-algodream-expertjob"

Sample Output
true
"""


# O(nm) time | O(nm) space - where n is the length of the first string and m is the length of the second string
def interweavingStrings(one, two, three):
    pass


if __name__ == "__main__":
    print(interweavingStrings("algoexpert", "your-dream-job", "your-algodream-expertjob"))
