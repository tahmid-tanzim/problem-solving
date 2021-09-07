#!/usr/bin/python3


def flatten_array(arr):
    v = []
    for a in arr:
        if type(a) is list:
            v += flatten_array(a)
        else:
            v.append(a)
    return v


def sum_flatten_array(arr):
    add = 0
    for a in arr:
        if type(a) is int:
            add += a
        else:
            add += sum_flatten_array(a)
    return add


if __name__ == '__main__':
    # print(flatten_array([1, 2, [3, 4, [5, [6], 7, [8, 9], 10], 11], [12, [13], 14], 15]))
    print(sum_flatten_array([1, 2, [3, 4, [5, [6], 7, [8, 9], 10], 11], [12, [13], 14], 15]))
