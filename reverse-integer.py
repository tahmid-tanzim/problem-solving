#!/usr/bin/python3
# https://leetcode.com/problems/reverse-integer/


def reverse(x: int) -> int:
    result = 0
    remainder = abs(x)
    while remainder != 0:
        result *= 10
        result += remainder % 10
        remainder //= 10
    if result > 2 ** 31:
        return 0
    return result if x >= 0 else -result


if __name__ == '__main__':
    # print('123 | ', reverse(123))
    # print('-123 | ', reverse(-123))
    # print('120 | ', reverse(120))
    # print('0 | ', reverse(0))
    print('1534236469 | ', reverse(1534236469), 9646324351)
