#!/usr/bin/python3
# https://leetcode.com/problems/plus-one/


def plus_one(digits):
    multiple = pow(10, len(digits) - 1)
    total = 1
    for d in digits:
        total += d * multiple
        multiple = multiple // 10

    output = []
    while True:
        output.insert(0, total % 10)
        total = total // 10
        if total == 0:
            break
    return output


if __name__ == '__main__':
    print(plus_one([1, 2, 3]))
    print(plus_one([4, 3, 2, 1]))
    print(plus_one([4, 1]))
    print(plus_one([5]))
