#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
from typing import List


# Sum formula
# Time O(n), n is the length of A
# Space O(1)
def findPermMissingElem(A: List[int]):
    n = len(A)
    if n == 0:
        return 1
    actual_sum = int(n * (n + 1) / 2)
    current_sum = 0
    for v in A:
        if v < n:
            current_sum += v
    return actual_sum - current_sum


# Sum formula
# Time O(n), n is the length of A
# Space O(1)
def findPermMissingElem2(A: List[int]):
    n = len(A)
    total = int((n + 1) * (n + 2) / 2)
    for v in A:
        total -= v
    return total


# XOR formula, int overflow will not occur
# Time O(n), n is the length of A
# Space O(1)
def findPermMissingElemXOR(A: List[int]):
    n = len(A)
    if n == 0:
        return 1
    x1 = A[0]  # XOR for all the element in array
    i = 1
    while i < n:
        x1 = x1 ^ A[i]
        i += 1

    x2 = 1  # XOR for all the element from 1 to n+1, because n+1 is included in the array
    i = 2
    while i <= n + 1:
        x2 = x2 ^ i
        i += 1

    return x1 ^ x2


if __name__ == '__main__':
    inputs = (
        {
            "A": [2, 3, 1, 5],
            "expected": 4
        },
        {
            "A": [],
            "expected": 1
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findPermMissingElem(val["A"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
