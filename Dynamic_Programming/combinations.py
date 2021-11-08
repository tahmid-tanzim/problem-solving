#!/usr/bin/python3
# https://leetcode.com/problems/combinations/
from typing import List


# Recursive, Memoization
# O(n ^ k) time, O(k) space
class Solution1:
    def combine(self, n: int, k: int, index: int = 1, STACK=[]) -> List[List[int]]:
        if k == 0:
            return [STACK]

        MERGED_STACK = list()
        while index <= n:
            tempStack = STACK.copy()
            tempStack.append(index)
            MERGED_STACK += self.combine(n, k - 1, index + 1, tempStack)
            index += 1
        return MERGED_STACK


if __name__ == "__main__":
    obj = Solution1()

    # print(obj.combine(4, 2))
    # Output:
    # [
    #   [2,4],
    #   [3,4],
    #   [2,3],
    #   [1,2],
    #   [1,3],
    #   [1,4],
    # ]

    # print(obj.combine(1, 1))
    # Output: [[1]]

    print(obj.combine(5, 3))
