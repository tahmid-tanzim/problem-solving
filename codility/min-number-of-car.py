#!/usr/bin/python3
from typing import List

"""
Task 2 - 15%

A group of friends is going on a holiday together. They have come to a meeting point
(the start of the journey) using N cars. There are P[K] people and S[K] seats in the
K-th car for K in range [0..N-1]. Some seats in the cars may be free, so it is 
possible for some friends to change the car they are in. the friends have decided that,
in order to be ecological, they will leave some cars parked at the meeting point and 
travel with as few cars as possible.

Write a function that given two arrays P and S, consists of N integers each, return the
minimum number of cars needed to take all friend on holiday.

Examples
1. Given P = [1, 4, 1] and S = [1, 5, 1], The function should return 2
2. Given P = [4, 4, 2, 4] and S = [5, 5, 2, 5], The function should return 3
3. Given P = [2, 3, 4, 2] and S = [2, 5, 7, 2], The function should return 2
 
Write an efficient algorithms for following assumptions:
    - N is an integer within the range [1..100,000]
    - each element of array P and S is an integer within the range [1..9]
    - P[K] <= S[K] for each K within the range [0..N-1]
"""


def findMinNumberOfCar(P: List[int], S: List[int]) -> int:
    total_cars = len(P)
    filled_seat = list()
    empty_seat = list()

    for p, s in zip(P, S):
        if p == s:
            filled_seat.append(s)
        else:
            empty_seat.append(s - p)

    while len(filled_seat) > 0 and len(empty_seat) > 0:
        min_idx = filled_seat.index(min(filled_seat))
        max_idx = empty_seat.index(max(empty_seat))

        if filled_seat[min_idx] <= empty_seat[max_idx]:
            empty_seat[max_idx] -= filled_seat[min_idx]
            del filled_seat[min_idx]
            total_cars -= 1
        else:
            filled_seat[min_idx] -= empty_seat[max_idx]
            del empty_seat[max_idx]

    return total_cars


if __name__ == '__main__':
    inputs = (
        {
            "P": [1, 4, 1],
            "S": [1, 5, 1],
            "expected": 2
        },
        {
            "P": [4, 4, 2, 4],
            "S": [5, 5, 2, 5],
            "expected": 3
        },
        {
            "P": [2, 3, 4, 2],
            "S": [2, 5, 7, 2],
            "expected": 2
        },
        {
            "P": [1, 2, 3, 4, 5],
            "S": [1, 2, 3, 4, 5],
            "expected": 5
        },
        {
            "P": [1, 2, 3, 4, 5],
            "S": [1, 2, 4, 4, 5],
            "expected": 4
        },
        {
            "P": [1, 3, 4, 5],
            "S": [2, 3, 4, 5],
            "expected": 4
        },
        {
            "P": [1, 2, 1, 5, 3],
            "S": [1, 2, 1, 7, 3],
            "expected": 3
        },
        {
            "P": [1, 2, 3],
            "S": [1, 2, 3],
            "expected": 3
        },
    )

    test_passed = 0
    for i, val in enumerate(inputs):
        output = findMinNumberOfCar(val["P"], val["S"])
        if output == val['expected']:
            print(f"{i}. CORRECT Answer\nOutput:{output}\nExpected:{val['expected']}\n\n")
            test_passed += 1
        else:
            print(f"{i}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n\n")

    print(f"Passed - {test_passed}/{i + 1}")
