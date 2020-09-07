#!/usr/local/bin/python3.6

"""
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""


def maximum69_number(num):
    arr = []
    while num != 0:
        i = num % 10
        arr.insert(0, i)
        num = num // 10
    size = len(arr)
    number = 0
    not_found = True
    for i in range(len(arr)):
        size -= 1
        if arr[i] == 6 and not_found:
            arr[i] = 9
            not_found = False
        number += arr[i] * 10 ** size
    return number


if __name__ == '__main__':
    print(maximum69_number(9669))
    print(maximum69_number(9996))
    print(maximum69_number(9999))

