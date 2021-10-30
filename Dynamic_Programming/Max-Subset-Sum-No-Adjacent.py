#!/usr/bin/python3
# https://www.algoexpert.io/questions/Max%20Subset%20Sum%20No%20Adjacent


# O(n) time, O(1) space
def maxSubsetSumNoAdjacent(array):
    # Base Case
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    maxSum = [array[0], max(array[0], array[1])]
    i = 2
    while i < len(array):
        include = maxSum[i - 2] + array[i]
        exclude = maxSum[i - 1]
        maxSum.append(max(include, exclude))
        i += 1
    return maxSum[-1]


if __name__ == '__main__':
    # Output ~> 330 = 75 + 120 + 135
    print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))
