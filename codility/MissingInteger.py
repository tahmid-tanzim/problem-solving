#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
from typing import List


# Time O(n * log(n))
# Space O(1)
def findMissingInteger(A: List[int]) -> int:
    A.sort()
    smallest_positive_integer = 1
    for value in A:
        if value > smallest_positive_integer:
            return smallest_positive_integer
        elif value == smallest_positive_integer:
            smallest_positive_integer += 1
    return smallest_positive_integer


# Time O(n)
# Space O(n)
def findMissingInteger2(A: List[int]) -> int:
    n = len(A)
    seen = [False] * n
    for value in A:
        if 1 <= value <= n:
            seen[value - 1] = True

    for i in range(n):
        if not seen[i]:
            return i + 1
    return n + 1


if __name__ == '__main__':
    inputs = (
        {
            "A": [1, 3, 6, 4, 1, 2],
            "expected": 5
        },
        {
            "A": [1, 2, 3],
            "expected": 4
        },
        {
            "A": [-1, -3],
            "expected": 1
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findMissingInteger2(val["A"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
