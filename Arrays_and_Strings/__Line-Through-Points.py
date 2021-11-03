#!/usr/bin/python3
# https://www.algoexpert.io/questions/Line%20Through%20Points
"""
  You're given an array of points plotted on a 2D graph (the xy-plane). Write a
  function that returns the maximum number of points that a single line (or
  potentially multiple lines) on the graph passes through.

  The input array will contain points represented by an array of two integers
  [x, y]. The input array will never contain duplicate points and
  will always contain at least one point.

Sample Input
points = [
  [1, 1],
  [2, 2],
  [3, 3],
  [0, 4],
  [-2, 6],
  [4, 0],
  [2, 1],
]

Sample Output
4 // A line passes through points: [-2, -6], [0, 4], [2, 2], [4, 0].
"""


# O(n^2) time | O(n) space
def lineThroughPoints(points):
    return 0


if __name__ == '__main__':
    print(lineThroughPoints([
        [1, 1],
        [2, 2],
        [3, 3],
        [0, 4],
        [-2, 6],
        [4, 0],
        [2, 1],
    ]))
