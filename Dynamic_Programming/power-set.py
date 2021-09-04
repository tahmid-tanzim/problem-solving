#!/usr/bin/python3
# Cracking the Coding Interview - 8.4
# Dynamic Programming - Power Set
from typing import List


# Solution 1 - Recursion
# O(n * 2^n)
def getSubsets(S: List[int], index: int) -> List[List[int]]:
    allSubsets = list()
    if len(S) == index:
        allSubsets.append([])
    else:
        allSubsets = getSubsets(S, index + 1)
        item: int = S[index]

        moreSubsets = list()
        for subset in allSubsets:
            newSubset = list()
            newSubset += subset
            newSubset.append(item)
            moreSubsets.append(newSubset)
        allSubsets += moreSubsets
    return allSubsets


def get_subset(nums: List[int]) -> List[List[int]]:
    allSubsets = [[]]

    for item in nums:
        n = len(allSubsets)
        for i in range(n):
            subset = allSubsets[i].copy()
            subset.append(item)
            allSubsets.append(subset)
    return allSubsets


if __name__ == "__main__":
    print(f"Answer - {getSubsets([1, 2, 3], 0)}")
