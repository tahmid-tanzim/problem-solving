#!/usr/bin/python3
# https://leetcode.com/problems/combination-sum-ii/
from typing import List
"""
Time Limit Exceed.
Need to implement a number frequency counter in Solution1
"""


# Backtracking with Index
# O(2^n) time, O(n) space
class Solution1:
    def __init__(self):
        self.combination = None

    def combinationSum2Helper(self, candidates: List[int], target: int, index: int, results: List[List[int]]) -> List[List[int]]:
        if target == 0:
            results.append(list(self.combination))
            return

        for next_index in range(index, len(candidates)):
            if next_index > index and candidates[next_index] == candidates[next_index - 1]:
                continue
            if target - candidates[next_index] < 0:
                break

            self.combination.append(candidates[next_index])
            self.combinationSum2Helper(candidates, target - candidates[next_index], next_index + 1, results)
            self.combination.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.combination = list()
        results = list()
        self.combinationSum2Helper(candidates, target, 0, results)
        return results


# Backtracking with Index & Build result in recursive callback
# O(2^n) time, O(n) space
class Solution2:
    def combinationSum2Helper(self, candidates: List[int], target: int, index: int, combination: List[int]) -> List[List[int]]:
        if target == 0:
            return [combination]
        if target < 0:
            return list()

        results = list()
        for next_index in range(index, len(candidates)):
            if next_index > index and candidates[next_index] == candidates[next_index - 1]:
                continue
            if target - candidates[next_index] < 0:
                break

            temp = combination.copy()
            temp.append(candidates[next_index])
            results += self.combinationSum2Helper(candidates, target - candidates[next_index], next_index + 1, temp)
        return results

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.combinationSum2Helper(candidates, target, 0, [])


# Run Time Exceed Limit
class Solution3:
    def __init__(self):
        self.CACHE = None

    def combinationSum2Helper(self, candidates: List[int], target: int, i: int = 0, STACK=[]) -> List[List[int]]:
        if target == 0:
            key = ":".join(str(x) for x in STACK)
            if key in self.CACHE:
                return []
            else:
                self.CACHE[key] = key
                return [STACK]
        if target < 0:
            return list()

        MERGE_STACK = list()
        while i < len(candidates):
            tempStack = STACK.copy()
            tempStack.append(candidates[i])
            MERGE_STACK += self.combinationSum2Helper(candidates, target - candidates[i], i + 1, tempStack)
            i += 1
        return MERGE_STACK

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.CACHE = dict()
        return self.combinationSum2Helper(candidates, target)


if __name__ == "__main__":
    obj = Solution2()

    print(obj.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    # Output:
    # [
    # [1,1,6],
    # [1,2,5],
    # [1,7],
    # [2,6]
    # ]

    print(obj.combinationSum2([2, 5, 2, 1, 2], 5))
    # Output:
    # [
    # [1,2,2],
    # [5]
    # ]

    print(obj.combinationSum2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 27))
