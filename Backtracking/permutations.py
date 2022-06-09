#!/usr/bin/python3
# https://leetcode.com/problems/permutations/
from typing import List

"""
([1,2,3], [])

([2,3], [1]) - ([1,3], [2]) - ([1,2], [3])

([3], [1,2]) -> ([], [1,2,3])
([2], [1,3]) -> ([], [1,3,2])

([3], [2,1]) -> ([], [2,1,3])
([1], [2,3]) -> ([], [2,3,1])

([2], [3,1]) -> ([], [3,1,2])
([1], [3,2]) -> ([], [3,2,1])
"""


class Solution:
    def __init__(self):
        self.result = []

    def dfs(self, nums: List[int], items: List[int]):
        n = len(nums)
        if n == 0:
            self.result.append(items)
            return

        for i in range(n):
            self.dfs(nums[0:i] + nums[i + 1:n], items + [nums[i]])

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.dfs(nums, [])
        return self.result

    def permute2(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        if n == 1:
            return [
                nums[:]
            ]

        for i in range(n):
            value = nums.pop(0)
            items = self.permute2(nums)
            for item in items:
                item.append(value)
            result += items
            nums.append(value)
        return result


if __name__ == "__main__":
    inputs = (
        {
            "nums": [1, 2, 3],
            "expected": [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1]
            ]
        },
        {
            "nums": [0, 1],
            "expected": [
                [0, 1],
                [1, 0]
            ]
        },
        {
            "nums": [1],
            "expected": [
                [1],
            ]
        },
    )

    obj = Solution()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.permute2(val["nums"])
        if sorted(output) == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")
    print(f"Passed: {test_passed:3}/{idx + 1}\n")
