#!/usr/bin/python3
# https://www.algoexpert.io/questions/Max%20Sum%20Increasing%20Subsequence
"""
  Write a function that takes in a non-empty array of integers and returns the
  greatest sum that can be generated from a strictly-increasing subsequence in
  the array as well as an array of the numbers in that subsequence.

  A subsequence of an array is a set of numbers that aren't necessarily adjacent
  in the array but that are in the same order as they appear in the array. For
  instance, the numbers [1, 3, 4] form a subsequence of the array
  [1, 2, 3, 4], and so do the numbers [2, 4]. Note
  that a single number in an array and the array itself are both valid
  subsequences of the array.

  You can assume that there will only be one increasing subsequence with the
  greatest sum.

Sample Input
array = [10, 70, 20, 30, 50, 11, 30]

Sample Output
[110, [10, 20, 30, 50]] // The subsequence [10, 20, 30, 50] is strictly increasing and yields the greatest sum: 110.
"""


# Dynamic Programming
class Solution1:
    @staticmethod
    def buildSequence(array, sequences, index):
        output = []
        while index is not None:
            output.insert(0, array[index])
            index = sequences[index]
        return output

    def maxSumIncreasingSubsequence(self, array):
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
        return sums[maxSumIdx], self.buildSequence(array, sequences, maxSumIdx)


class Solution2:
    # Brute Force Solution
    @staticmethod
    def maxSumIncreasingSubsequence(array):
        allSubsequence = list()

        for num in array:
            n = len(allSubsequence)
            if n > 0:
                for i in range(n):
                    subsequence = allSubsequence[i]
                    if num > subsequence[-1] and subsequence[-1] < 0:
                        allSubsequence[i].pop(-1)
                        allSubsequence[i].append(num)
                    if num > subsequence[-1] > 0:
                        allSubsequence[i].append(num)
                    if num < subsequence[-1]:
                        tempSubsequence = subsequence.copy()
                        while len(tempSubsequence) > 0:
                            lastItem = tempSubsequence.pop(-1)
                            if lastItem < num:
                                tempSubsequence.append(lastItem)
                                break
                        tempSubsequence.append(num)
                        allSubsequence.append(tempSubsequence)
            else:
                allSubsequence.append([num])

        result = [float('-inf'), None]
        for subsequence in allSubsequence:
            total = sum(subsequence)
            if total > result[0]:
                result = [total, subsequence]

        return result


if __name__ == "__main__":
    obj = Solution1()
    print(f'OUTPUT {obj.maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30])}')
    obj = Solution2()
    print(f'OUTPUT {obj.maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30])}')