#!/usr/bin/python3
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
from typing import List


"""
# Time O(n^2)
# Space O(1)
# Time Limit Exceeded
def replaceElements(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n - 1):
        next_max = 0
        for j in range(i + 1, n):
            if next_max < arr[j]:
                next_max = arr[j]
        arr[i] = next_max
    arr[n - 1] = -1
    return arr
"""


# Time O(n)
# Space O(1)
def replaceElements(arr: List[int]) -> List[int]:
    n = len(arr)
    right_max = arr[n - 1]
    arr[n - 1] = -1
    for i in range(n - 2, -1, -1):
        if arr[i] > right_max:
            temp = right_max
            right_max = arr[i]
            arr[i] = temp
        else:
            arr[i] = right_max
    return arr


if __name__ == '__main__':
    inputs = (
        {
            "arr": [17, 18, 5, 4, 6, 1],
            "expected": [18, 6, 6, 6, 1, -1]
        },
        {
            "arr": [400],
            "expected": [-1]
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = replaceElements(val["arr"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
