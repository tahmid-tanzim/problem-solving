#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/6-sorting/distinct/
from typing import List


# Time O(n)
# Space O(n)
def findDistinct(A: List[int]) -> int:
    distinctSet = set()
    for value in A:
        distinctSet.add(value)
    return len(distinctSet)


if __name__ == '__main__':
    inputs = (
        {
            "A": [2, 1, 1, 2, 3, 1],
            "expected": 3
        },
        {
            "A": [-1000000, 2, 1, 1, 2, 3, -1000000, 1000000],
            "expected": 5
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findDistinct(val["A"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
