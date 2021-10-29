#!/usr/bin/python3
# https://www.algoexpert.io/questions/Suffix%20Trie%20Construction


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

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

    def contains(self, string):
        current_node = self.root
        for letter in string:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        return self.endSymbol in current_node


if __name__ == "__main__":
    obj = SuffixTrie("babc")
    print(obj.contains("abc"))  # True
    print(obj.contains("ab"))  # False
