#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/3-time_complexity/
# from typing import List

"""
FrogJmp

A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Write an efficient algorithm for the following assumptions:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.
"""


# O(1)
def findFrogJmp(X: int, Y: int, D: int):
    from math import ceil
    return ceil((Y - X) / D)


# O(y)
def findFrogJmp2(X: int, Y: int, D: int):
    jump = 0
    for step in range(X, Y, D):
        jump += 1
    return jump


if __name__ == '__main__':
    inputs = (
        {
            "X": 10,
            "Y": 85,
            "D": 30,
            "expected": 3
        },
        {
            "X": 10,
            "Y": 41,
            "D": 30,
            "expected": 2
        },
        {
            "X": 30,
            "Y": 35,
            "D": 10,
            "expected": 1
        },
        {
            "X": 30,
            "Y": 30,
            "D": 10,
            "expected": 0
        },
        {
            "X": 10,
            "Y": 30,
            "D": 0.75,
            "expected": 27
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findFrogJmp(val["X"], val["Y"], val["D"])
        print(output)
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
