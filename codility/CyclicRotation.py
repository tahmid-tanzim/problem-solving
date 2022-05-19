#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
from typing import List


# O(n*K), n is the length of A
def findCyclicRotation(A: List[int], K: int):
    n = len(A)
    if n == 0:
        return []

    K = K % n

    while K > 0:
        i = n - 2
        while i >= 0:
            temp = A[i + 1]
            A[i + 1] = A[i]
            A[i] = temp
            i -= 1
        K -= 1
    return A


if __name__ == '__main__':
    inputs = (
        {
            "A": [3, 8, 9, 7, 6],
            "K": 3,
            "expected": [9, 7, 6, 3, 8]
        },
        {
            "A": [0, 0, 0],
            "K": 1,
            "expected": [0, 0, 0]
        },
        {
            "A": [1, 2, 3, 4],
            "K": 4,
            "expected": [1, 2, 3, 4]
        },
        {
            "A": [],
            "K": 4,
            "expected": []
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findCyclicRotation(val["A"], val["K"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
