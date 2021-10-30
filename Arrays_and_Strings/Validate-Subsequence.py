#!/usr/bin/python3
# https://www.algoexpert.io/questions/Validate%20Subsequence
"""
The second array must be subsequence of first array.
For instance, the numbers [1, 3, 4] and [2, 4] form a subsequence of the array [1, 2, 3, 4]
"""


# Time Complexity - O(n)
# Space Complexity - O(1)
def isValidSubsequence(array, sequence):
    p = 0
    for i in array:
        if p == len(sequence):
            return True
        if i == sequence[p]:
            p += 1
    return p == len(sequence)


if __name__ == '__main__':
    output1 = isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])  # True
    print(f'{output1}')
