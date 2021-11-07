#!/usr/bin/python3
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
"""
You have d dice and each die has f faces numbered 1, 2, ..., f. 
You are given three integers d, f, and target.

Return the number of possible ways (out of fd total ways) modulo 109 + 7 to roll the dice 
so the sum of the face-up numbers equals target.
"""


# Recursive, Memoization
# O(f ^ d) time, O(d) space
# f is numberOfFace & d is numberOfDice
class Solution1:
    def calculateWays(self, numberOfDice: int, numberOfFace: int, target: int, MEMO_HASHTABLE):
        if numberOfDice == 0:
            if target == 0:
                return 1
            else:
                return 0

        key = f"{numberOfDice}:{target}"
        if key in MEMO_HASHTABLE:
            return MEMO_HASHTABLE[key]

        ways = 0
        for faceValue in range(1, numberOfFace + 1):
            ways += self.calculateWays(numberOfDice - 1, numberOfFace, target - faceValue, MEMO_HASHTABLE)
        MEMO_HASHTABLE[key] = ways
        return ways

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MEMO_HASHTABLE = dict()
        return self.calculateWays(d, f, target, MEMO_HASHTABLE) % (10**9 + 7)


if __name__ == "__main__":
    obj = Solution1()
    # print(obj.numRollsToTarget(1, 6, 3))  # 1
    # print(obj.numRollsToTarget(2, 6, 7))  # 6
    # print(obj.numRollsToTarget(2, 5, 10))  # 1
    # print(obj.numRollsToTarget(1, 2, 3))  # 0
    print(obj.numRollsToTarget(30, 30, 500))  # 222616187
