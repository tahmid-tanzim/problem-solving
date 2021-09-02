#!/usr/bin/python3

"""
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""


def subtract_product_and_sum(n):
    product = 1
    add = 0
    while n != 0:
        i = n % 10
        add += i
        product *= i
        n = n // 10
    return product - add


if __name__ == '__main__':
    print(subtract_product_and_sum(234))
    print(subtract_product_and_sum(4421))

