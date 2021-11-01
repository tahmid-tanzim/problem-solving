#!/usr/bin/python3
# https://www.algoexpert.io/questions/Water%20Area
"""
  You're given an array of non-negative integers where each non-zero integer
  represents the height of a pillar of width 1. Imagine water being
  poured over all of the pillars; write a function that returns the surface area
  of the water trapped between the pillars viewed from the front. Note that
  spilled water should be ignored.

  You can refer to the first three minutes of this question's video explanation
  for a visual example.

Sample Input
heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]

Sample Output
48

// Below is a visual representation of the sample input.
// The dots and vertical lines represent trapped water and pillars, respectively.
// Note that there are 48 dots.
//        |
//        |
//  |.....|
//  |.....|
//  |.....|
//  |..|..|
//  |..|..|
//  |..|..|.....|
//  |..|..|.....|
// _|..|..|..||.|
"""


# O(n) time, O(n) space
def waterArea1(heights):
    n = len(heights)
    leftMaxHeights = [0]
    rightMaxHeights = [0]

    maxHeights = 0
    for i in range(1, n):
        if heights[i - 1] > maxHeights:
            maxHeights = heights[i - 1]
        leftMaxHeights.append(maxHeights)

    maxHeights = 0
    for i in range(n - 2, -1, -1):
        if heights[i + 1] > maxHeights:
            maxHeights = heights[i + 1]
        rightMaxHeights.insert(0, maxHeights)

    totalWater = 0
    for i in range(n):
        heightAtIndex = heights[i]
        minBoundary = min(leftMaxHeights[i], rightMaxHeights[i])
        if minBoundary > heightAtIndex:
            totalWater += minBoundary - heightAtIndex

    return totalWater


# O(n) time, O(n) space
def waterArea2(heights):
    n = len(heights)
    leftMaxHeights = list()
    rightMaxHeights = list()

    maxHeights = 0
    for i in range(n):
        leftMaxHeights.append(maxHeights)
        if heights[i] > maxHeights:
            maxHeights = heights[i]

    maxHeights = 0
    for i in range(n - 1, -1, -1):
        rightMaxHeights.insert(0, maxHeights)
        if heights[i] > maxHeights:
            maxHeights = heights[i]

    totalWater = 0
    for i in range(n):
        heightAtIndex = heights[i]
        minBoundary = min(leftMaxHeights[i], rightMaxHeights[i])
        if minBoundary > heightAtIndex:
            totalWater += minBoundary - heightAtIndex

    return totalWater


if __name__ == "__main__":
    print(waterArea1([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
    print(waterArea2([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
