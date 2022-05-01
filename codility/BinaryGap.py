#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/1-iterations/
"""
BinaryGap

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by
ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
The number 20 has binary representation 10100 and contains one binary gap of length 1.
The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000
and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and
so its longest binary gap is of length 5. Given N = 32 the function should return 0,
because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""


def findBinaryGap(n: int):
    max_gap = 0
    binary = str(bin(n))
    i = 2
    counter = 0
    found_start_one = False
    # print(n, binary)
    while i < len(binary):
        # print(n, i, binary[i])
        if binary[i] == '0' and found_start_one:
            counter += 1
        elif binary[i] == '1':
            if counter > max_gap:
                max_gap = counter
            counter = 0
            found_start_one = True
        i += 1
    return max_gap


if __name__ == '__main__':
    inputs = (
        {
            "N": 9,
            "expected": 2
        },
        {
            "N": 529,
            "expected": 4
        },
        {
            "N": 20,
            "expected": 1
        },
        {
            "N": 15,
            "expected": 0
        },
        {
            "N": 32,
            "expected": 0
        },
        {
            "N": 1,
            "expected": 0
        },
        {
            "N": 2147483647,
            "expected": 0
        },
        {
            "N": 2147483645,
            "expected": 1
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findBinaryGap(val["N"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:{output:9}\nExpected:{val['expected']:7}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output:9}\nExpected:{val['expected']:7}\n")

    print(f"Passed: {test_passed:6}/{idx + 1}\n")
