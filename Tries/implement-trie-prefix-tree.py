#!/usr/bin/python3
# https://leetcode.com/problems/implement-trie-prefix-tree/


class Trie:
    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.isEndOfWord = False

    def insert(self, word: str) -> None:
        currentNode = self
        for letter in word:
            if letter in currentNode.children:
                currentNode = currentNode.children[letter]
            else:
                newNode = Trie(letter)
                currentNode.children[letter] = newNode
                currentNode = newNode
        currentNode.isEndOfWord = True

    def search(self, word: str) -> bool:
        currentNode = self
        for letter in word:
            if letter not in currentNode.children:
                return False
            currentNode = currentNode.children[letter]
        return currentNode.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        currentNode = self
        for letter in prefix:
            if letter not in currentNode.children:
                return False
            currentNode = currentNode.children[letter]
        return True


if __name__ == "__main__":
    # Your Trie object will be instantiated and called as such:
    obj = Trie()
    obj.insert("apple")
    print(obj.search("apple"))
    print(obj.search("app"))
    print(obj.startsWith("app"))
    obj.insert("app")
    print(obj.search("app"))
