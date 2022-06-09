#!/usr/bin/python3
# https://leetcode.com/problems/permutations-ii/
from typing import List


class Solution:
    def backtrack(self, counter, combination, n, result):
        if len(combination) == n:
            result.append(combination)
            return

        for num in counter:
            if counter[num] > 0:
                counter[num] -= 1
                self.backtrack(counter, combination + [num], n, result)
                counter[num] += 1

    # Time Complexity O(n * n!)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        result = []
        self.backtrack(counter, [], len(nums), result)
        return result


if __name__ == "__main__":
    inputs = (
        {
            "nums": [1, 1, 2],
            "expected": [
                [1, 1, 2],
                [1, 2, 1],
                [2, 1, 1],
            ]
        },
        {
            "nums": [1, 2, 3],
            "expected": [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1]
            ],
        },
    )

    obj = Solution()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.permuteUnique(val["nums"])
        if sorted(output) == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")
    print(f"Passed: {test_passed:3}/{idx + 1}\n")
