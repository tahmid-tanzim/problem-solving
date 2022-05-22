#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
from typing import List


# Time O(N * M), N is number of counters & M is the length of A
# Space O(N)
def findMaxCounters(N: int, A: List[int]) -> List[int]:
    counters = [0] * N
    max_value = None

    for value in A:
        if 1 <= value <= N:
            counters[value - 1] += 1
            if max_value is None or counters[value - 1] > max_value:
                max_value = counters[value - 1]
        elif value == N + 1:
            for i in range(N):
                counters[i] = max_value

    return counters


# Time O(N + M), N is number of counters & M is the length of A
# Space O(N)
def findMaxCounters2(N: int, A: List[int]) -> List[int]:
    counters = [0] * N
    current_max = 0
    last_max = 0

    for value in A:
        if 1 <= value <= N:
            counters[value - 1] = max(counters[value - 1], last_max)
            counters[value - 1] += 1

            current_max = max(current_max, counters[value - 1])
        elif value == N + 1:
            last_max = current_max

    for i in range(N):
        counters[i] = max(counters[i], last_max)

    return counters


if __name__ == '__main__':
    inputs = (
        {
            "A": [3, 4, 4, 6, 1, 4, 4],
            "N": 5,
            "expected": [3, 2, 2, 4, 2]
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findMaxCounters2(val["N"], val["A"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
