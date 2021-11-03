#!/usr/bin/python3
# https://www.algoexpert.io/questions/Non-Attacking%20Queens
"""
  Write a function that takes in a positive integer n and returns
  the number of non-attacking placements of n queens on an n x n chessboard.

  A non-attacking placement is one where no queen can attack another queen in a
  single turn. In other words, it's a placement where no queen can move to the
  same position as another queen in a single turn.

  In chess, queens can move any number of squares horizontally, vertically, or
  diagonally in a single turn.

+--+--+--+--+  
|  |Q |  |  |
+--+--+--+--+
|  |  |  |Q |
+--+--+--+--+
|Q |  |  |  |
+--+--+--+--+
|  |  |Q |  |
+--+--+--+--+

  The chessboard above is an example of a non-attacking placement of 4 queens on
  a 4x4 chessboard. For reference, there are only 2 non-attacking placements of
  4 queens on a 4x4 chessboard.

Sample Input
n = 4

Sample Output
2
"""


# Upper Bound: O(n!) time | O(n) space - where n is the input number
def nonAttackingQueens(n):
    return 0


if __name__ == "__main__":
    print(nonAttackingQueens(4))
