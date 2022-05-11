#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/2-arrays/
from typing import List

"""
OddOccurrencesInArray

A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
"""


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
