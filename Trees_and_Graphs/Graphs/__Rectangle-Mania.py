#!/usr/bin/python3
# https://www.algoexpert.io/questions/Rectangle%20Mania
"""
  Write a function that takes in a list of Cartesian coordinates (i.e., (x, y)
  coordinates) and returns the number of rectangles formed by these coordinates.

  A rectangle must have its four corners amongst the coordinates in order to be
  counted, and we only care about rectangles with sides parallel to the x and y
  axes (i.e., with horizontal and vertical sides--no diagonal sides).

  You can also assume that no coordinate will be farther than 100 units from the origin.

Sample Input
coords = [
  [0, 0], [0, 1], [1, 1], [1, 0],
  [2, 1], [2, 0], [3, 1], [3, 0],
]

Sample Output
6
"""


def rectangleMania(coords):
    pass


if __name__ == "__main__":
    print(rectangleMania([
        [0, 0], [0, 1], [1, 1], [1, 0],
        [2, 1], [2, 0], [3, 1], [3, 0],
    ]))
