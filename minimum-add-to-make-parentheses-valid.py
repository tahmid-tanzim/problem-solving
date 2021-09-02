#!/usr/bin/python3

"""
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
"""


def min_add_to_make_valid(S):
    stack = list()
    counter = 0
    for char in S:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) > 0:
                stack.pop(-1)
            else:
                counter += 1
    return counter + len(stack)


if __name__ == '__main__':
    print(min_add_to_make_valid("())"))
    print(min_add_to_make_valid("((("))
    print(min_add_to_make_valid("()"))
    print(min_add_to_make_valid("()))(("))

    # _test = list()
    # _test.append('a')
    # _test.append('b')
    # _test.append('c')
    # print(_test)
    # last = _test.pop(-1)
    # print(_test, last)
