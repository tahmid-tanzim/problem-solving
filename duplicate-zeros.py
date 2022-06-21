#!/usr/bin/python3
# https://leetcode.com/problems/duplicate-zeros/submissions/
from typing import List


class Solution1:
    def duplicateZeros(self, arr: List[int]) -> List[int]:
        i = noOfExtraZeros = 0
        n = len(arr) - 1
        while n - i - noOfExtraZeros > 0:
            if arr[i] == 0:
                noOfExtraZeros += 1
            i += 1

        # Edge Case Handle Extra Leftover Zero in last index
        if arr[i] == 0 and i == n - noOfExtraZeros:
            arr[n] = 0
            n -= 1

        print(noOfExtraZeros)
        last = n - noOfExtraZeros
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + noOfExtraZeros] = 0
                noOfExtraZeros -= 1
                arr[i + noOfExtraZeros] = 0
            else:
                arr[i + noOfExtraZeros] = arr[i]
        return arr


class Solution2:
    def duplicateZeros(self, arr: List[int]) -> List[int]:
        possible_dups = 0
        length_ = len(arr) - 1

        # Find the number of zeros to be duplicated
        for left in range(length_ + 1):

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > length_ - possible_dups:
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included
                if left == length_ - possible_dups:
                    arr[length_] = 0  # For this zero we just copy it without duplication.
                    length_ -= 1
                    break
                possible_dups += 1

        print(possible_dups)
        # Start backwards from the last element which would be part of new list.
        last = length_ - possible_dups

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]

        return arr


class Solution3:
    def duplicateZeros(self, arr: List[int]) -> List[int]:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0
        return arr


if __name__ == '__main__':
    inputs = (
        {
            "arr": [9,9,9,4,8,0,0,3,7,2,0,0,0,0,9,1,0,0,1,1,0,5,6,3,1,6,0,0,2,3,4,7,0,3,9,3,6,5,8,9,1,1,3,2,0,0,7,3,3,0,5,7,0,8,1,9,6,3,0,8,8,8,8,0,0,5,0,0,0,3,7,7,7,7,5,1,0,0,8,0,0],
            "expected": [9,9,9,4,8,0,0,0,0,3,7,2,0,0,0,0,0,0,0,0,9,1,0,0,0,0,1,1,0,0,5,6,3,1,6,0,0,0,0,2,3,4,7,0,0,3,9,3,6,5,8,9,1,1,3,2,0,0,0,0,7,3,3,0,0,5,7,0,0,8,1,9,6,3,0,0,8,8,8,8,0]
        },
        {
            "arr": [1,0,2,3,0,4,5,0],
            "expected": [1,0,0,2,3,0,0,4]
        },
        {
            "arr": [1,2,3],
            "expected": [1,2,3]
        },
        {
            "arr": [8,4,5,0,0,0,0,7],
            "expected": [8,4,5,0,0,0,0,0]
        },
        {
            "arr": [9,0,9,0,6,0,0,0,1,1,6,5,4,4,8,3,0,0,0,1,5,3,0,0,7,2,1,0,2,0,9,1,0,2,0,0,0,0,0,0,0,6,0,0,7,9,0,8,7,0,9,7,1,0,2,0,0,0,0,9,0,0,0,0],
            "expected": [9,0,0,9,0,0,6,0,0,0,0,0,0,1,1,6,5,4,4,8,3,0,0,0,0,0,0,1,5,3,0,0,0,0,7,2,1,0,0,2,0,0,9,1,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0]
        },
    )

    test_passed = 0
    obj = Solution3()
    for idx, val in enumerate(inputs):
        output = obj.duplicateZeros(val["arr"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:   {output}\nExpected: {val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
