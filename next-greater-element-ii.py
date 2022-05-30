#!/usr/bin/python3
# https://leetcode.com/problems/next-greater-element-ii/
from typing import List


# Time O(n)
# Space O(1)
def nextGreaterElements(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(n):
        while len(stack) > 0 and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)

    while len(stack) > 0:
        j = stack.pop()
        for i in range(j):
            if nums[i] > nums[j]:
                result[j] = nums[i]
                break
    return result


if __name__ == '__main__':
    inputs = (
        {
            "nums": [1, 2, 1],
            "expected": [2, -1, 2]
        },
        {
            "nums": [1, 2, 3, 4, 3],
            "expected": [2, 3, 4, -1, 4]
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = nextGreaterElements(val["nums"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
