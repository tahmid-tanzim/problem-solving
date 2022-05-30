#!/usr/bin/python3
# https://leetcode.com/problems/next-greater-element-i/
from typing import List


# Time O(n)
# Space O(1)
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1Index = {}
    for i, n1 in enumerate(nums1):
        nums1Index[n1] = i
        nums1[i] = -1

    n = len(nums2)
    stack = []
    for i in range(n):
        while len(stack) > 0 and nums2[i] > stack[-1]:
            value = stack.pop()
            index = nums1Index[value]
            nums1[index] = nums2[i]
        if nums2[i] in nums1Index:
            stack.append(nums2[i])
    return nums1


if __name__ == '__main__':
    inputs = (
        {
            "nums1": [4, 1, 2],
            "nums2": [1, 3, 4, 2],
            "expected": [-1, 3, -1]
        },
        {
            "nums1": [2, 4],
            "nums2": [1, 2, 3, 4],
            "expected": [3, -1]
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = nextGreaterElement(val["nums1"], val["nums2"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
