#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
from typing import List


# Time O(n^2), n is the length of A
# Space O(1)
def findPermCheck(A: List[int]) -> int:
    n = len(A)
    total_passing_car = 0
    for i in range(n - 1):
        if A[i] == 0:
            for j in range(i + 1, n):
                if A[j] == 1:
                    total_passing_car += 1
    return total_passing_car


# Time O(n), n is the length of A
# Space O(n)
def findPermCheck2(A: List[int]) -> int:
    totalPassingCar = 0
    noOfEastCar = 0
    for car_type in A:
        if totalPassingCar > 1000000000:
            return -1
        if car_type == 0:
            noOfEastCar += 1
        else:
            totalPassingCar += car_type * noOfEastCar
    return totalPassingCar


if __name__ == '__main__':
    inputs = (
        {
            "A": [0, 1, 0, 1, 1],
            "expected": 5
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findPermCheck2(val["A"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
