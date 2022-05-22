#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/6-sorting/distinct/
from typing import List


# Time O(n^3)
# Space O(1)
def findMaxProductOfThree(A: List[int]) -> int:
    n = len(A)
    maxProductOfTriplet = None
    for p in range(n - 2):
        for q in range(p + 1, n - 1):
            for r in range(q + 1, n):
                productOfTriplet = A[p] * A[q] * A[r]
                if maxProductOfTriplet is None or maxProductOfTriplet < productOfTriplet:
                    maxProductOfTriplet = productOfTriplet
    return maxProductOfTriplet


# Time O(n * log(n))
# Space O(1)
def findMaxProductOfThree2(A: List[int]) -> int:
    A.sort()
    option = A[-3] * A[-2] * A[-1]
    if A[0] <= A[1] < 0:
        option = max(option, A[0] * A[1] * A[-1])
    return option


if __name__ == '__main__':
    inputs = (
        {
            "A": [-3, 1, 2, -2, 5, 6],
            "expected": 60
        },
        {
            "A": [-5, 5, -5, 4],
            "expected": 125
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findMaxProductOfThree2(val["A"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
