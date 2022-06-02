#!/usr/bin/python3
# https://leetcode.com/problems/word-search/
from typing import List


class Solution:
    # Time Complexity O(r * c * 4^n) where n is the length of word
    def dfs(self, board: List[List[str]], word: str, r: int, row: int, c: int, col: int, i: int, path: set) -> bool:
        if i == len(word):
            return True
        if r < 0 or r >= row or c < 0 or c >= col or word[i] != board[r][c] or (r, c) in path:
            return False
        path.add((r, c))

        result = self.dfs(board, word, r - 1, row, c, col, i + 1, path) or \
                 self.dfs(board, word, r + 1, row, c, col, i + 1, path) or \
                 self.dfs(board, word, r, row, c - 1, col, i + 1, path) or \
                 self.dfs(board, word, r, row, c + 1, col, i + 1, path)
        path.remove((r, c))
        return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        for r in range(row):
            for c in range(col):
                if self.dfs(board, word, r, row, c, col, 0, set()):
                    return True
        return False


if __name__ == "__main__":
    inputs = (
        {
            "board": [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"]
            ],
            "word": "ABCCED",
            "expected": True,
        },
        {
            "board": [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"]
            ],
            "word": "SEE",
            "expected": True,
        },
        {
            "board": [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"]
            ],
            "word": "ABCB",
            "expected": False,
        },
        {
            "board": [
                ["a"]
            ],
            "word": "a",
            "expected": True,
        },
    )

    obj = Solution()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.exist(val["board"], val["word"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")
    print(f"Passed: {test_passed:3}/{idx + 1}\n")
