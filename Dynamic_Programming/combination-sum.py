#!/usr/bin/python3
# https://leetcode.com/problems/combination-sum/
from typing import List


# Recursive, Memoization
# O(n ^ t) time, O(n ^ t) space
class Solution1:
    def combinationSumHelper(self, candidates: List[int], target: int, index, DP) -> List[List[int]]:
        if target == 0:
            return [DP]
        if target < 0:
            return list()

        currentIdx = index
        output = list()
        while currentIdx < len(candidates):
            tempDP = DP.copy()
            tempDP.append(candidates[currentIdx])
            output += self.combinationSumHelper(candidates, target - candidates[currentIdx], currentIdx, tempDP)
            currentIdx += 1
        return output

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.combinationSumHelper(candidates, target, 0, list())


if __name__ == "__main__":
    obj = Solution1()

    print(obj.combinationSum([2, 3, 6, 7], 7))
    # Output: [[2,2,3],[7]]
    # Explanation:
    # 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    # 7 is a candidate, and 7 = 7.
    # These are the only two combinations.

    print(obj.combinationSum([2, 3, 5], 8))
    # # Output: [[2,2,2,2],[2,3,3],[3,5]]
    #
    print(obj.combinationSum([2], 1))
    # # Output: []
    #
    print(obj.combinationSum([1], 1))
    # # Output: [[1]]
    #
    print(obj.combinationSum([1], 2))
    # # Output: [[1,1]]
