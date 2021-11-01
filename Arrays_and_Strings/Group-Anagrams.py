#!/usr/bin/python3
# https://www.algoexpert.io/questions/Group%20Anagrams
"""
  Write a function that takes in an array of strings and groups anagrams together.

  Anagrams are strings made up of exactly the same letters, where order doesn't
  matter. For example, "cinema" and "iceman" are
  anagrams; similarly, "foo" and "ofo" are anagrams.

  Your function should return a list of anagram groups in no particular order.

Sample Input
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

Sample Output
[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
"""


# O(w * n * log(n)) time | O(wn) space
# where w is the number of words and n is the length of the longest word
def groupAnagrams(words):
    anagram_group = dict()

    for word in words:
        sorted_word = str().join(sorted(word))
        if sorted_word in anagram_group:
            anagram_group[sorted_word].append(word)
        else:
            anagram_group[sorted_word] = [word]

    return list(anagram_group.values())


if __name__ == '__main__':
    output1 = groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"])
    print(f'{output1}')
