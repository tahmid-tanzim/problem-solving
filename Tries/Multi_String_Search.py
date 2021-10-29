#!/usr/bin/python3
# https://www.algoexpert.io/questions/Multi%20String%20Search


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # O(n^2) time | O(n^2) space
    def insertSubstringStartingAt(self, i, string):
        current_node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in current_node:
                current_node[letter] = dict()
            current_node = current_node[letter]
        current_node[self.endSymbol] = True

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    # O(n) time | O(1) space
    def contains(self, string):
        current_node = self.root
        for letter in string:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        return True


def multiStringSearch(bigString, smallStrings):
    obj = SuffixTrie(bigString)
    return [obj.contains(smallString) for smallString in smallStrings]


if __name__ == "__main__":
    # print(multiStringSearch("this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]))
    # print(multiStringSearch("abcdefghijklmnopqrstuvwxyz", ["abc", "mnopqr", "wyz", "no", "e", "tuuv"]))

    # Expected Output - [false, false, false, false, true, false, false]
    print(multiStringSearch("adcb akfkw afnmc fkadn vkaca jdaf dacb cdba cbda",
                            ["abcd", "acbd", "adbc", "dabc", "cbda", "cabd", "cdab"]))  # False
