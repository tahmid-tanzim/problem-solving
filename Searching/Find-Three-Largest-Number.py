#!/usr/bin/python3
# https://www.algoexpert.io/questions/Find%20Three%20Largest%20Numbers
"""
  The function should return duplicate integers if necessary; for example, it
  should return [10, 10, 12] for an input array of
  [10, 5, 9, 10, 12].
"""


def findThreeLargestNumbers(array):
    largest_numbers = array[0:3]
    largest_numbers.sort()
    i = 3
    while i < len(array):
        if array[i] > largest_numbers[0]:
            largest_numbers[0] = array[i]
            for x in range(2):
                if largest_numbers[x] > largest_numbers[x + 1]:
                    temp = largest_numbers[x]
                    largest_numbers[x] = largest_numbers[x + 1]
                    largest_numbers[x + 1] = temp
        i += 1
    return largest_numbers


if __name__ == '__main__':
    print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
