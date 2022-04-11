#!/usr/bin/python3
# https://leetcode.com/problems/find-lucky-integer-in-an-array/


def find_lucky(arr):
    result = -1
    frequency = dict()
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    for key in frequency:
        if key == frequency[key] and result < key:
            result = key
    return result


if __name__ == "__main__":
    print(find_lucky([2, 2, 3, 4]))  # 2
    print(find_lucky([1, 2, 2, 3, 3, 3]))  # 3
    print(find_lucky([2, 2, 2, 3, 3]))  # -1
    print(find_lucky([1, 2, 3, 4]))  # 1
    print(find_lucky([5]))  # -1
