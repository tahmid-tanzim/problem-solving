#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
from typing import List


# Time O(n), n is the length of A
# Space O(n)
def findPermCheck(A: List[int]) -> int:
    n = len(A)
    permutation = [False] * n
    for value in A:
        if value > n or permutation[value - 1]:  # Out of range or repeated
            return 0
        permutation[value - 1] = True
    return 1


if __name__ == '__main__':
    inputs = (
        {
            "A": [4, 1, 3, 2],
            "expected": 1
        },
        {
            "A": [4, 1, 3],
            "expected": 0
        },
        {
            "A": [3, 2, 1, 3],
            "expected": 0
        },
        {
            "A": [3, 2, 1, 4, 2],
            "expected": 0
        },
        {
            "A": [3, 2, 1, 4, 6],
            "expected": 0
        },
        {
            "A": [4, 1, 7, 2],
            "expected": 0
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findPermCheck(val["A"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
