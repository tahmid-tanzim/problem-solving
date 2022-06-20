#!/usr/bin/python3
# https://leetcode.com/problems/word-search-ii/
from typing import List


class Trie:
    def __init__(self, char=None):
        self.char: str = char
        self.children = {}
        self.isEndOfWord = False

    def addWord(self, word):
        currentNode = self
        for letter in word:
            if letter in currentNode.children:
                currentNode = currentNode.children[letter]
            else:
                newNode = Trie(letter)
                currentNode.children[letter] = newNode
                currentNode = newNode
        currentNode.isEndOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rootNode = Trie()
        for word in words:
            rootNode.addWord(word)

        result = set()
        visited = set()
        row = len(board)
        col = len(board[0])

        def dfs(r: int, c: int, node, word):
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] not in node.children or (r, c) in visited:
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isEndOfWord:
                result.add(word)

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            visited.remove((r, c))

        for r in range(row):
            for c in range(col):
                dfs(r, c, rootNode, "")

        return list(result)


def load_inputs():
    import json
    file = open("testcase/word-search-ii.json")
    data = json.load(file)
    file.close()
    return data


if __name__ == "__main__":
    inputs = load_inputs()

    obj = Solution()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.findWords(val["board"], val["words"])
        if sorted(output) == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")
    print(f"Passed: {test_passed:3}/{idx + 1}\n")
