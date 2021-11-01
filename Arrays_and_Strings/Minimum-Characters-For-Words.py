#!/usr/bin/python3
# https://www.algoexpert.io/questions/Minimum%20Characters%20For%20Words
"""
  Write a function that takes in an array of words and returns the smallest
  array of characters needed to form all of the words. The characters don't need
  to be in any particular order.

  For example, the characters ["y", "r", "o", "u"] are needed to
  form the words ["your", "you", "or", "yo"].

  Note: the input words won't contain any spaces; however, they might contain
  punctuation and/or special characters.

Sample Input
words = ["this", "that", "did", "deed", "them!", "a"]

Sample Output
["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
// The characters could be ordered differently.
"""


# O(n * l) time | O(c) space
# where n is the number of words,
# l is the length of the longest word,
# and c is the number of unique characters across all words
def minimumCharactersForWords(words):
    frequency = dict()
    for word in words:
        lettersInWord = dict()
        for letter in word:
            if letter in lettersInWord:
                lettersInWord[letter] += 1
            else:
                lettersInWord[letter] = 1

            if letter not in frequency or lettersInWord[letter] > frequency[letter]:
                frequency[letter] = lettersInWord[letter]

    output = list()
    for key, value in frequency.items():
        output += [key] * value

    return output


if __name__ == '__main__':
    output1 = minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"])
    print(f'{output1}')
