#!/usr/bin/python3
# https://www.algoexpert.io/questions/Staircase%20Traversal
"""
  You're given two positive integers representing the height of a staircase and
  the maximum number of steps that you can advance up the staircase at a time.
  Write a function that returns the number of ways in which you can climb the
  staircase.

  For example, if you were given a staircase of height = 3 and
  maxSteps = 2 you could climb the staircase in 3 ways. You could
  take 1 step, 1 step, then 1 step, you could also take
  1 step, then 2 steps, and you could take 2 steps, then 1 step.

Note that 'maxSteps <= height' will always be true.
Sample Input
height = 4
maxSteps = 2

Sample Output
5
// You can climb the staircase in the following ways: 
// 1, 1, 1, 1
// 1, 1, 2
// 1, 2, 1
// 2, 1, 1
// 2, 2
"""


class Solution1:
    # Recursive Solution (Memoization)
    def staircaseTraversal(self, height, maxSteps):
        return self.numberOfWaysToHeight(height, maxSteps, {0: 1, 1: 1})

    # O(n * k) time | O(n) space
    def numberOfWaysToHeight(self, height, maxSteps, matrix):
        if height in matrix:
            return matrix[height]

        step = 1
        numberOfWays = 0
        while step <= min(maxSteps, height):
            numberOfWays += self.numberOfWaysToHeight(height - step, maxSteps, matrix)
            step += 1

        matrix[height] = numberOfWays
        return numberOfWays


class Solution2:
    # Dynamic Programming
    # O(n * k) time | O(n) space
    @staticmethod
    def staircaseTraversal(height, maxSteps):
        # Initialize
        numberOfWays = [0] * (height + 1)
        numberOfWays[0], numberOfWays[1] = 1, 1

        currentHeight = 2
        while currentHeight <= height:
            step = 1
            while step <= maxSteps and step <= currentHeight:
                numberOfWays[currentHeight] += numberOfWays[currentHeight - step]
                step += 1
            currentHeight += 1

        return numberOfWays[height]


class Solution3:
    # Sliding Window
    # O(n) time | O(n) space
    @staticmethod
    def staircaseTraversal(height, maxSteps):
        currentNumberOfWays = 0
        waysToTop = [1]

        for currentHeight in range(1, height + 1):
            startOfWindow = currentHeight - maxSteps - 1
            endOfWindow = currentHeight - 1

            if startOfWindow >= 0:
                currentNumberOfWays -= waysToTop[startOfWindow]

            currentNumberOfWays += waysToTop[endOfWindow]
            waysToTop.append(currentNumberOfWays)

        return currentNumberOfWays


if __name__ == "__main__":
    s1 = Solution1()
    print(s1.staircaseTraversal(4, 2))
    s2 = Solution2()
    print(s2.staircaseTraversal(4, 2))
    s3 = Solution3()
    print(s3.staircaseTraversal(4, 2))
