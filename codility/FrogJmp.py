#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
# from typing import List


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
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
