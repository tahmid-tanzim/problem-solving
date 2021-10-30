#!/usr/bin/python3
# https://www.algoexpert.io/questions/Product%20Sum
"""
  A "special" array is a non-empty array that contains either integers or other
  "special" arrays. The product sum of a "special" array is the sum of its
  elements, where "special" arrays inside it are summed themselves and then
  multiplied by their level of depth.

  The depth of a "special" array is how far nested it is. For instance, the
  depth of [] is 1; the depth of the inner array in
  [[]] is 2; the depth of the innermost array in
  [[[]]] is 3.

  Therefore, the product sum of [x, y] is x + y; the
  product sum of [x, [y, z]] is x + 2 * (y + z); the
  product sum of [x, [y, [z]]] is x + 2 * (y + 3z).
"""


def calculate(array, depth):
    total = 0
    for item in array:
        if type(item) is list:
            total += calculate(item, depth + 1)
        else:
            total += item
    return total * depth


def productSum(array):
    depth = 1
    return calculate(array, depth)


if __name__ == "__main__":
    output = productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])  # 12
    print(f'Output - {output}')

