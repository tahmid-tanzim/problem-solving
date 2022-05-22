#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/6-sorting/triangle/
from typing import List


# Time O(n^3)
# Space O(1)
def findTriangle(A: List[int]) -> int:
    n = len(A)
    for p in range(n - 2):
        for q in range(p + 1, n - 1):
            for r in range(q + 1, n):
                if A[p] + A[q] > A[r] and A[q] + A[r] > A[p] and A[r] + A[p] > A[q]:
                    return 1
    return 0


# Time O(n * log(n))
# Space O(1)
def findTriangle2(A: List[int]) -> int:
    n = len(A)
    if n < 3:
        return 0

    A.sort()
    for i in range(n - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1
    return 0


if __name__ == '__main__':
    inputs = (
        {
            "A": [10, 2, 5, 1, 8, 20],
            "expected": 1
        },
        {
            "A": [10, 50, 5, 1],
            "expected": 0
        },
        {
            "A": [1, 1, 1, 1, 5, 5, 5],
            "expected": 1
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findTriangle(val["A"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
