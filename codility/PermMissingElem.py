#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
from typing import List

"""
PermMissingElem

An array A consisting of N different integers is given. 
The array contains integers in the range [1..(N + 1)], 
which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
"""


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
