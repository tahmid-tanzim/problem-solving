#!/usr/bin/python3
# https://www.algoexpert.io/questions/Youngest%20Common%20Ancestor
"""
  You're given three inputs, all of which are instances of an
  AncestralTree class that have an ancestor property
  pointing to their youngest ancestor. The first input is the top ancestor in an
  ancestral tree (i.e., the only instance that has no ancestor--its
  ancestor property points to None / null), and the other two inputs are descendants in the ancestral tree.

  Write a function that returns the youngest common ancestor to the two
  descendants.

  Note that a descendant is considered its own ancestor. So in the simple
  ancestral tree below, the youngest common ancestor to nodes A and B is node A.

// The youngest common ancestor to nodes A and B is node A.
  A
 /
B

Sample Input
// The nodes are from the ancestral tree below.
topAncestor = node A
descendantOne = node E
descendantTwo = node I
          A
       /     \
      B       C
    /   \   /   \
   D     E F     G
 /   \
H     I

Sample Output
node B
"""


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getDescendantDepth(topAncestor, descendant):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth


# O(d) time, O(1) space
# d is the height of the ancestral tree
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(topAncestor, descendantOne)
    depthTwo = getDescendantDepth(topAncestor, descendantTwo)

    if depthOne > depthTwo:
        lowerDescendant, higherDescendant = descendantOne, descendantTwo
        diff = depthOne - depthTwo
    else:
        lowerDescendant, higherDescendant = descendantTwo, descendantOne
        diff = depthTwo - depthOne

    while diff > 0:
        diff -= 1
        lowerDescendant = lowerDescendant.ancestor
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return higherDescendant


if __name__ == "__main__":
    pass
