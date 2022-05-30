#!/usr/bin/python3
# https://leetcode.com/problems/largest-rectangle-in-histogram/
from typing import List


# Time O(n)
# Space O(1)
def largestRectangleArea(heights: List[int]) -> int:
    n = len(heights)

    # Right Smaller Element
    rightSmallerElement = [n] * n
    indexStack = []
    for i in range(n):
        while len(indexStack) > 0 and heights[i] < heights[indexStack[-1]]:
            index = indexStack.pop()
            rightSmallerElement[index] = i
        indexStack.append(i)
    # print(rightSmallerElement)

    # Left Smaller Element
    leftSmallerElement = [-1] * n
    indexStack = []
    for i in range(n - 1, -1, -1):
        while len(indexStack) > 0 and heights[i] < heights[indexStack[-1]]:
            index = indexStack.pop()
            leftSmallerElement[index] = i
        indexStack.append(i)
    # print(leftSmallerElement)

    # Calculate Max Area
    maxRectangleArea = 0
    for i in range(n):
        area = (rightSmallerElement[i] - leftSmallerElement[i] - 1) * heights[i]
        if area > maxRectangleArea:
            maxRectangleArea = area
    return maxRectangleArea


if __name__ == '__main__':
    inputs = (
        {
            "heights": [2, 1, 5, 6, 2, 3],
            "expected": 10
        },
        {
            "heights": [2, 4],
            "expected": 4
        },
        {
            "heights": [1, 1],
            "expected": 2
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = largestRectangleArea(val["heights"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
