#!/usr/bin/python3
# https://www.algoexpert.io/questions/Laptop%20Rentals
"""
  You're given a list of time intervals during which students at a school need a
  laptop. These time intervals are represented by pairs of integers
  [start, end], where 0 &lt;= start &lt; end. However,
  start and end don't represent real times; therefore, they may be greater than 24.

  No two students can use a laptop at the same time, but immediately after a
  student is done using a laptop, another student can use that same laptop. For
  example, if one student rents a laptop during the time interval
  [0, 2], another student can rent the same laptop during any time interval starting with 2.

  Write a function that returns the minimum number of laptops that the school
  needs to rent such that all students will always have access to a laptop when they need one.

Sample Input
times = 
[
  [0, 2],
  [1, 4],
  [4, 6],
  [0, 4],
  [7, 8],
  [9, 11],
  [3, 10],
]

Sample Output
3
"""


# O(nlog(n)) time | O(n) space
# where n is the number of times
def laptopRentals(times):
    n = len(times)
    if n == 0:
        return n

    startTime = list()
    endTime = list()
    for [start, end] in times:
        startTime.append(start)
        endTime.append(end)
    startTime.sort()
    endTime.sort()

    numberOfLaptops = 0
    i = j = 0

    while i < n:
        if startTime[i] >= endTime[j]:
            numberOfLaptops -= 1
            j += 1

        numberOfLaptops += 1
        i += 1

    return numberOfLaptops


if __name__ == '__main__':
    print(laptopRentals([
        [0, 2],
        [1, 4],
        [4, 6],
        [0, 4],
        [7, 8],
        [9, 11],
        [3, 10],
    ]))
