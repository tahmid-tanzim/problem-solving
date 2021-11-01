#!/usr/bin/python3
# https://www.algoexpert.io/questions/Reverse%20Words%20In%20String
"""
  Write a function that takes in a string of words separated by one or more
  whitespaces and returns a string that has these words in reverse order. For
  example, given the string "tim is great", your function should
  return "great is tim".

  For this problem, a word can contain special characters, punctuation, and
  numbers. The words in the string will be separated by one or more whitespaces,
  and the reversed string must contain the same whitespaces as the original
  string. For example, given the string
  "whitespaces    4" you would be expected to return
  "4    whitespaces".

  Note that you're not allowed to to use any built-in
  split or reverse methods/functions. However, you
  are allowed to use a built-in join method/function.

Also note that the input string isn't guaranteed to always contain words.
Sample Input
string = "AlgoExpert is the best!"

Sample Output
"best! the is AlgoExpert"
"""


# Time Complexity - O(n)
# Space Complexity - O(n)
def reverseWordsInString(string):
    reversedString = ""
    startIndx = 0
    endIndx = 0
    while endIndx < len(string):
        if string[endIndx] == ' ':
            reversedString = string[startIndx:endIndx] + ' ' + reversedString
            startIndx = endIndx + 1
        endIndx += 1
    reversedString = string[startIndx:endIndx] + ' ' + reversedString

    return reversedString[:-1]


if __name__ == '__main__':
    output1 = reverseWordsInString("AlgoExpert is the best!")
    print(f'{output1}')
