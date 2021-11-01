#!/usr/bin/python3
# https://www.algoexpert.io/questions/Min%20Number%20Of%20Jumps
"""
  You're given a non-empty array of positive integers where each integer represents the
  maximum number of steps you can take forward in the array. For example, if the
  element at index 1 is 3, you can go from index
  1 to index 2, 3, or 4.

  Write a function that returns the minimum number of jumps needed to reach the
  final index.

  Note that jumping from index i to index i + x always
  constitutes one jump, no matter how large x is.

Sample Input
array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]

Sample Output
4 // 3 --> (4 or 2) --> (2 or 3) --> 7 --> 3
"""


# O(n^2) time | O(n) space
class Solution1:
    @staticmethod
    def minNumberOfJumps(array):
        n = len(array)
        jumps = [float('inf') if i > 0 else 0 for i in range(n)]

        for i in range(1, n):
            for j in range(i):
                if array[j] + j >= i:
                    if jumps[j] + 1 < jumps[i]:
                        jumps[i] = jumps[j] + 1

        return jumps[n - 1]


# O(n) time | O(1) space
class Solution2:
    @staticmethod
    def minNumberOfJumps(array):
        if len(array) == 1:
            return 0

        jumps = 0
        maxReach = array[0]
        steps = array[0]

        for i in range(1, len(array) - 1):
            maxReach = max(maxReach, i + array[i])
            steps -= 1
            if steps == 0:
                jumps += 1
                steps = maxReach - i

        return jumps + 1


if __name__ == "__main__":
    obj = Solution1()
    print(obj.minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
    obj = Solution2()
    print(obj.minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
