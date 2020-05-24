#!/usr/local/bin/python3.6

"""
https://leetcode.com/problems/check-if-a-string-can-break-another-string/
"""


def check_if_can_break(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    n = len(s1)
    for i in range(n):
        if s1[i] >= s2[i]:
            return False
    return True


if __name__ == '__main__':
    print(check_if_can_break("abc", "xya"))
    print(check_if_can_break("abe", "acd"))
    print(check_if_can_break("leetcodee", "interview"))
