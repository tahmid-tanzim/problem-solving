#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/8-leader/dominator/
from typing import List


# Time O(n)
# Space O(n)
def findDominator(A: List[int]) -> int:
    n = len(A)
    frequency = {}
    index = 0
    for value in A:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

        if frequency[value] > (n // 2):
            return index
        index += 1
    return -1


if __name__ == '__main__':
    inputs = (
        {
            "A": [3, 4, 3, 2, 3, -1, 3, 3],
            "expected": (0, 2, 4, 6, 7,)
        },
        {
            "A": [6, 8, 4, 6, 8, 6, 6],
            "expected": (0, 3, 5, 6,)
        },
        {
            "A": [1, 2, 3, 2, 2],
            "expected": (1, 3, 4,)
        },
        {
            "A": [1, 2, 3],
            "expected": (-1,)
        },
        {
            "A": [1, 1, 2, 2, 3],
            "expected": (-1,)
        },
        {
            "A": [],
            "expected": (-1,)
        },
        {
            "A": [5],
            "expected": (0,)
        },
        {
            "A": [2147483647],
            "expected": (0,)
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findDominator(val["A"])
        if output in val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
