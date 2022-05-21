#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
from typing import List


# Time O(n^2), n is the length of A
# Space O(1)
def findTapeEquilibrium(A: List[int]):
    n = len(A)
    min_diff = None
    for p in range(1, n):
        left_sum = right_sum = 0

        for left_idx in range(0, p):
            left_sum += A[left_idx]

        for right_idx in range(p, n):
            right_sum += A[right_idx]

        absolute_diff = abs(left_sum - right_sum)
        if min_diff is None or absolute_diff < min_diff:
            min_diff = absolute_diff

    return min_diff


# Time O(n), n is the length of A
# Space O(1)
def findTapeEquilibrium2(A: List[int]):
    n = len(A)
    total = 0
    for value in A:
        total += value

    min_diff = None
    left_sum = 0
    for i in range(n - 1):
        left_sum += A[i]
        absolute_diff = abs(total - left_sum * 2)
        if min_diff is None or absolute_diff < min_diff:
            min_diff = absolute_diff

    return min_diff


if __name__ == '__main__':
    inputs = (
        {
            "A": [3, 1, 2, 4, 3],
            "expected": 1
        },
        {
            "A": [5, 9],
            "expected": 4
        },
        {
            "A": [-1000, 1000],
            "expected": 2000
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findTapeEquilibrium2(val["A"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
