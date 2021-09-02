#!/usr/bin/python3
# https://leetcode.com/problems/first-unique-character-in-a-string/


def first_uniq_char(s):
    i = 0
    while i < len(s):
        if s[i] not in s[:i] + s[i+1:]:
            return i
        i += 1
    return -1


if __name__ == '__main__':
    print(first_uniq_char("leetcode"))  # 0
    print(first_uniq_char("loveleetcode"))  # 2
    print(first_uniq_char("oceodced"))  # -1
