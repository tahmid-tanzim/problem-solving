#!/usr/bin/python3

"""
https://leetcode.com/problems/create-target-array-in-the-given-order/
"""


def create_target_array(nums, index):
    target = list()
    for i in range(len(nums)):
        target = target[:index[i]] + [nums[i]] + target[index[i]:]
    return target


if __name__ == '__main__':
    print(create_target_array(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]))
    print(create_target_array(nums=[1, 2, 3, 4, 0], index=[0, 1, 2, 3, 0]))
    print(create_target_array(nums=[1], index=[0]))
