#!/usr/bin/python3
# https://www.algoexpert.io/questions/Minimum%20Area%20Rectangle
"""
  You're given an array of points plotted on a 2D graph (the xy-plane). Write a
  function that returns the minimum area of any rectangle that can be formed
  using any 4 of these points such that the rectangle's sides are parallel to
  the x and y axes (i.e., only rectangles with horizontal and vertical sides
  should be considered--no rectangles with diagonal sides). If no rectangle can
  be formed, your function should return 0.

  The input array will contain points represented by arrays of two integers
  [x, y]. The input array will never contain duplicate points.

Sample Input
points = 
[
  [1, 5],
  [5, 1],
  [4, 2],
  [2, 4],
  [2, 2],
  [1, 2],
  [4, 5],
  [2, 5],
  [-1, -2],
]

Sample Output
3
// The rectangle with corners [1, 5], [2, 5], [1, 2], and [2, 2]
// has the minimum area: 3.
"""


# O(n^2) time | O(n) space
def minimumAreaRectangle(points):
    return 0


if __name__ == '__main__':
    print(minimumAreaRectangle([
        [1, 5],
        [5, 1],
        [4, 2],
        [2, 4],
        [2, 2],
        [1, 2],
        [4, 5],
        [2, 5],
        [-1, -2],
    ]))
