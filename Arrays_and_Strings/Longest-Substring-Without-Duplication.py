#!/usr/bin/python3
# https://www.algoexpert.io/questions/Longest%20Substring%20Without%20Duplication
"""
  Write a function that takes in a string and returns its longest substring
  without duplicate characters.

You can assume that there will only be one longest substring without duplication.
Sample Input
string = "clementisacap"

Sample Output
"mentisac"
"""


# O(n) time | O(min(n, a)) space
# where n is the length of the input string and
# a is the length of the character alphabet represented in the input string
def longestSubstringWithoutDuplication(string):
    n = len(string)
    maxLength = 0
    longestSubstr = str()
    currentSubstr = str()
    for i in range(n):
        currentLength = len(currentSubstr)
        for j in range(currentLength):
            if currentSubstr[j] == string[i]:
                if currentLength > maxLength:
                    maxLength = currentLength
                    longestSubstr = currentSubstr
                currentSubstr = currentSubstr[j + 1:i]
                break
        currentSubstr += string[i]

    # Check Last currentSunstr
    return currentSubstr if len(currentSubstr) > maxLength else longestSubstr


if __name__ == '__main__':
    output1 = longestSubstringWithoutDuplication("clementisacap")
    print(f'{output1}')
