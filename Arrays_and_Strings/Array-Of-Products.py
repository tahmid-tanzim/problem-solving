#!/usr/bin/python3
# https://www.algoexpert.io/questions/Array%20Of%20Products
"""
  Write a function that takes in a non-empty array of integers and returns an
  array of the same length, where each element in the output array is equal to
  the product of every other number in the input array.

  In other words, the value at output[i] is equal to the product of
  every number in the input array other than input[i].

Note that you're expected to solve this problem without using division.
Sample Input
array = [5, 1, 4, 2]

Sample Output
[8, 40, 10, 20]
// 8 is equal to 1 x 4 x 2
// 40 is equal to 5 x 4 x 2
// 10 is equal to 5 x 1 x 2
// 20 is equal to 5 x 1 x 4
"""


# Time - O(n^2) | Space O(n)
def arrayOfProducts1(array):
    total_product = []
    for i, val in enumerate(array):
        current_product = 1
        for j, _ in enumerate(array):
            if i != j:
                current_product *= array[j]
        total_product.append(current_product)
    return total_product


# Time - O(n) | Space O(n)
def arrayOfProducts2(array):
    n = len(array)
    total_product = []
    leftProduct = 1
    rightProduct = 1

    for i in range(n):
        total_product.append(leftProduct)
        leftProduct *= array[i]

    for i in range(n - 1, -1, -1):
        total_product[i] *= rightProduct
        rightProduct *= array[i]

    return total_product


if __name__ == '__main__':
    output1 = arrayOfProducts1([5, 1, 4, 2])
    output2 = arrayOfProducts2([5, 1, 4, 2])

    print(f'{output1}')
    print(f'{output2}')
