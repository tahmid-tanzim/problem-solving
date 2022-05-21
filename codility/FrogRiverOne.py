#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
from typing import List


# Time O(n)
# Space O(n)
def findFrogRiverOne(X: int, A: List[int]) -> int:
    leaf_check = [False] * X
    sum_step = 0
    for sec, position in enumerate(A):
        if position <= X and not leaf_check[position - 1]:
            leaf_check[position - 1] = True
            sum_step += 1
            if sum_step == X:
                return sec
    return -1


if __name__ == '__main__':
    inputs = (
        {
            "A": [1, 3, 1, 4, 2, 3, 5, 4],
            "X": 5,
            "expected": 6
        },
        {
            "A": [3, 10, 8, 2, 3, 5, 9, 6, 1, 4, 8, 2, 1],
            "X": 7,
            "expected": -1
        },
        {
            "A": [13, 10, 2, 5, 6, 7, 1, 3, 4, 7, 9, 8, 10, 9, 10, 10],
            "X": 10,
            "expected": 11
        },
        {
            "A": [1],
            "X": 1,
            "expected": 0
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findFrogRiverOne(val["X"], val["A"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
