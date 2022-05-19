#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
from typing import List


def findOddOccurrences(A: List[int]):
    hashtable = {}
    for i in A:
        if i in hashtable:
            del hashtable[i]
        else:
            hashtable[i] = True

    key = list(hashtable.keys())
    return key[0] if len(key) > 0 else 0


if __name__ == '__main__':
    inputs = (
        {
            "A": [9, 3, 9, 3, 9, 7, 9],
            "expected": 7
        },

    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findOddOccurrences(val["A"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
