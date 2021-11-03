#!/usr/bin/python3
# https://www.algoexpert.io/questions/Continuous%20Median
"""
    Write a ContinuousMedianHandler class that supports:

    1. The continuous insertion of numbers with the insert method.
    2. The instant (O(1) time) retrieval of the median of the numbers that have
    been inserted thus far with the getMedian method.

  The getMedian method has already been written for you. You simply
  have to write the insert method.

  The median of a set of numbers is the "middle" number when the numbers are
  ordered from smallest to greatest. If there's an odd number of numbers in the
  set, as in {1, 3, 7}, the median is the number in the middle
  (3 in this case); if there's an even number of numbers in the
  set, as in {1, 3, 7, 8}, the median is the average of the two
  middle numbers ((3 + 7) / 2 == 5 in this case).

Sample Usage
// All operations below are performed sequentially.
ContinuousMedianHandler(): - // instantiate a ContinuousMedianHandler
insert(5): -
insert(10): -
getMedian(): 7.5
insert(100): -
getMedian(): 10
"""


# Insert: O(log(n)) time | O(n) space
# where n is the number of inserted numbers
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None

    def insert(self, number):
        # Write your code here.
        pass

    def getMedian(self):
        return self.median


if __name__ == '__main__':
    pass
