#!/usr/bin/python3
# https://www.algoexpert.io/questions/Single%20Cycle%20Check
"""
  You're given an array of integers where each integer represents a jump of its
  value in the array. For instance, the integer 2 represents a jump
  of two indices forward in the array; the integer -3 represents a
  jump of three indices backward in the array.

  If a jump spills past the array's bounds, it wraps over to the other side. For
  instance, a jump of -1 at index 0 brings us to the last index in
  the array. Similarly, a jump of 1 at the last index in the array brings us to
  index 0.

  Write a function that returns a boolean representing whether the jumps in the
  array form a single cycle. A single cycle occurs if, starting at any index in
  the array and following the jumps, every element in the array is visited
  exactly once before landing back on the starting index.
"""


# O(n) time, O(1) space
def hasSingleCycle(array):
    n = len(array)
    visitedCount = 0
    currentIdx = 0
    while visitedCount < n:
        if visitedCount > 0 and currentIdx == 0:
            return False
        visitedCount += 1

        # Update currentIdx with jump count
        jump = array[currentIdx]
        nextIdx = (currentIdx + jump) % n
        currentIdx = nextIdx if nextIdx >= 0 else nextIdx + n

    return currentIdx == 0


if __name__ == "__main__":
    print(hasSingleCycle([2, 3, 1, -4, -4, 2]))  # True
