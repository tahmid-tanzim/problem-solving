#!/usr/bin/python3

# Dynamic Programming
def buildSequence(array, sequences, index):
    output = []
    while index is not None:
        output.insert(0, array[index])
        index = sequences[index]
    return output


def maxSumIncreasingSubsequence(array):
    n = len(array)
    sequences = [None] * n
    sums = array.copy()
    maxSumIdx = 0
    for i in range(n):
        for j in range(0, i):
            if array[j] < array[i] and sums[j] + array[i] >= sums[i]:
                sums[i] = sums[j] + array[i]
                sequences[i] = j

        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i
    return sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)


if __name__ == "__main__":
    print(f'G1 {maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30])}')
