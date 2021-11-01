#!/usr/bin/python3
# https://www.algoexpert.io/questions/Powerset
"""
  Write a function that takes in an array of unique integers and returns its
  powerset.

  The powerset P(X) of a set X is the set of all
  subsets of X. For example, the powerset of [1,2] is
  [[], [1], [2], [1,2]].

  Note that the sets in the powerset do not need to be in any particular order.

Sample Input
array = [1, 2, 3]

Sample Output
[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
"""


# Iterative Solution
# Time - O(n * 2^n) | Space - O(n * 2^n)
def powersetIterative(array):
    subsets = [[]]

    for x in array:
        n = len(subsets) - 1
        while n >= 0:
            subsets.append(subsets[n] + [x])
            n -= 1

    return subsets


# Recursive Solution
# Time - O(n * 2^n) | Space - O(n * 2^n)
def powersetRecursive(array, idx=None):
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]

    val = array[idx]
    subsets = powersetRecursive(array, idx - 1)

    for i in range(len(subsets)):
        subsets.append(subsets[i] + [val])

    return subsets


if __name__ == "__main__":
    output = powersetIterative([1, 2, 3])
    print(f'Output - {output}')
    output = powersetRecursive([1, 2, 3])
    print(f'Output - {output}')

