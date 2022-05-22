#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
from typing import List


# Time O(B - A)
# Space O(1)
def findCountDiv(A: int, B: int, K: int) -> int:
    counter = 0
    for i in range(A, B + 1, K):
        if i % K == 0:
            counter += 1
    return counter


# Time O(1)
# Space O(1)
def findCountDiv2(A: int, B: int, K: int):
    return B // K - A // K + (1 if A % K == 0 else 0)


if __name__ == '__main__':
    inputs = (
        {
            "A": 6,
            "B": 11,
            "K": 2,
            "expected": 3
        },
        {
            "A": 1,
            "B": 2000000000,
            "K": 1,
            "expected": 2000000000
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findCountDiv2(val["A"], val["B"], val["K"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
