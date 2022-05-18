#!/usr/bin/python3
# https://leetcode.com/problems/car-pooling/
from typing import List


# Time O(nlog(n)), Space O(n)
def carPooling(trips: List[List[int]], capacity: int) -> bool:
    matrix = list()
    for numPassengers, startIdx, endIdx in trips:
        matrix.append((startIdx, 1, numPassengers,))
        matrix.append((endIdx, 0, numPassengers,))

    matrix.sort(key=lambda v: (v[0], v[1]))
    print(matrix)
    for i, isPassengerPickUP, numPassengers in matrix:
        if isPassengerPickUP == 1:
            if numPassengers > capacity:
                return False
            capacity -= numPassengers
        else:
            capacity += numPassengers

    return True


if __name__ == '__main__':
    inputs = (
        {
            "trips": [
                [2, 1, 5],
                [3, 3, 7],
            ],
            "capacity": 4,
            "expected": False
        },
        {
            "trips": [
                [2, 1, 5],
                [3, 3, 7],
            ],
            "capacity": 5,
            "expected": True
        },
        {
            "trips": [
                [4, 5, 6],
                [6, 4, 7],
                [4, 3, 5],
                [2, 3, 5]
            ],
            "capacity": 13,
            "expected": True
        },
        {
            "trips": [[1, 1, 4], [9, 4, 9], [9, 1, 9], [2, 3, 5], [4, 1, 5], [10, 4, 5]],
            "capacity": 33,
            "expected": False
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = carPooling(val["trips"], val["capacity"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
