#!/usr/bin/python3
# https://www.algoexpert.io/questions/Permutations
"""
  Write a function that takes in an array of unique integers and returns an
  array of all permutations of those integers in no particular order.

If the input array is empty, the function should return an empty array.
Sample Input
array = [1, 2, 3]

Sample Output
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""


# O(n*n!) time | O(n*n!) space
# where n is the length of the input array
def calculatePermutations(array):
    last_item = array.pop()
    if len(array) == 0:
        return [[last_item]]

    permutations = calculatePermutations(array)

    new_permutations = []
    for prev_permutation in permutations:
        for i in range(len(prev_permutation) + 1):
            temp = prev_permutation.copy()
            temp.insert(i, last_item)
            new_permutations.append(temp)

    return new_permutations


def getPermutations(array):
    if len(array) == 0:
        return []
    return calculatePermutations(array)


if __name__ == "__main__":
    output = getPermutations([1, 2, 3])
    print(f'Output - {output}')

