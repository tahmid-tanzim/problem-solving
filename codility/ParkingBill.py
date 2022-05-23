#!/usr/bin/python3
# https://app.codility.com/programmers/trainings/5/parking_bill/
import math


# Time O(1)
# Space O(1)
def findParkingBill(E: str, L: str) -> int:
    entryHH, entryMM = map(int, E.split(":"))
    exitHH, exitMM = map(int, L.split(":"))
    time_spend = (exitHH * 60 + exitMM) - (entryHH * 60 + entryMM)
    if time_spend == 0:
        return 0
    total_cost = 5
    time_spend -= 60.0
    total_cost += math.ceil(time_spend / 60) * 4
    return total_cost


if __name__ == '__main__':
    inputs = (
        {
            "E": "10:00",
            "L": "13:21",
            "expected": 17
        },
        {
            "E": "09:42",
            "L": "11:42",
            "expected": 9
        },
        {
            "E": "17:07",
            "L": "19:08",
            "expected": 13
        },
        {
            "E": "17:05",
            "L": "19:04",
            "expected": 9
        },
        {
            "E": "03:15",
            "L": "03:50",
            "expected": 5
        },
        {
            "E": "03:15",
            "L": "03:16",
            "expected": 5
        },
        {
            "E": "03:33",
            "L": "03:33",
            "expected": 0
        },
        {
            "E": "02:10",
            "L": "04:10",
            "expected": 9
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findParkingBill(val["E"], val["L"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
