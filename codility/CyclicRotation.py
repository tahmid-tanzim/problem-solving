#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
from typing import List

"""
CyclicRotation

An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""


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
