#!/usr/bin/python3
# https://www.algoexpert.io/questions/Underscorify%20Substring
"""
  Write a function that takes in two strings: a main string and a potential
  substring of the main string. The function should return a version of the main
  string with every instance of the substring in it wrapped between underscores.

  If two or more instances of the substring in the main string overlap each
  other or sit side by side, the underscores relevant to these substrings should
  only appear on the far left of the leftmost substring and on the far right of
  the rightmost substring. If the main string doesn't contain the other string
  at all, the function should return the main string intact.

Sample Input
string = "testthis is a testtest to see if testestest it works"
substring = "test"

Sample Output
"_test_this is a _testtest_ to see if _testestest_ it works"
"""


# Average case: O(n + m) | O(n) space
# where n is the length of the main string and m is the length of the substring
def underscorifySubstring(string, substring):
    pass


if __name__ == '__main__':
    print(underscorifySubstring("testthis is a testtest to see if testestest it works", "test"))
