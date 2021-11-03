#!/usr/bin/python3
# https://www.algoexpert.io/questions/Lowest%20Common%20Manager
"""
  You're given three inputs, all of which are instances of an
  OrgChart class that have a directReports property
  pointing to their direct reports. The first input is the top manager in an
  organizational chart (i.e., the only instance that isn't anybody else's direct
  report), and the other two inputs are reports in the organizational chart. The
  two reports are guaranteed to be distinct.

  Write a function that returns the lowest common manager to the two reports.

Sample Input
// From the organizational chart below.
topManager = Node A
reportOne = Node E
reportTwo = Node I
          A
       /     \
      B       C
    /   \   /   \
   D     E F     G
 /   \
H     I

Sample Output
Node B
"""


class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []


def getLowestCommonManager(topManager, reportOne, reportTwo):
    pass


if __name__ == "__main__":
    pass
