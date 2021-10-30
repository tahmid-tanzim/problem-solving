#!/usr/bin/python3
# https://www.algoexpert.io/questions/Generate%20Document
"""
  You're given a string of available characters and a string representing a
  document that you need to generate. Write a function that determines if you
  can generate the document using the available characters. If you can generate
  the document, your function should return true; otherwise, it
  should return false.

  You're only able to generate the document if the frequency of unique
  characters in the characters string is greater than or equal to the frequency
  of unique characters in the document string. For example, if you're given
  characters = "abcabc" and document = "aabbccc" you
  <b>cannot</b> generate the document because you're missing one c.

  The document that you need to create may contain any characters, including
  special characters, capital letters, numbers, and spaces.
"""


# O(n+m) time, O(c) space
# n is the number of characters,
# m is the length of the document
# c is number of unique letter in the characters string
def generateDocument(characters, document):
    hashtable = dict()
    for char in characters:
        if char not in hashtable:
            hashtable[char] = 0
        hashtable[char] += 1

    for char in document:
        if char in hashtable and hashtable[char] > 0:
            hashtable[char] -= 1
        else:
            return False

    return True


if __name__ == '__main__':
    print(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))  # True
