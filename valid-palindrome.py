#!/usr/bin/python3
# https://leetcode.com/problems/valid-palindrome/


def validate_alphanumeric(char):
    ASCII = ord(char)
    if 65 <= ASCII <= 90:
        ASCII += 32
    return chr(ASCII) if 48 <= ASCII <= 57 or 97 <= ASCII <= 122 else None


def is_palindrome(s):
    head, tail = 0, len(s) - 1

    while head < tail:
        h = validate_alphanumeric(s[head])
        t = validate_alphanumeric(s[tail])
        if h is None:
            head += 1
            continue
        if t is None:
            tail -= 1
            continue

        if h != t:
            return False
        else:
            head += 1
            tail -= 1
    return True


if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("race a car"))  # False
    print(is_palindrome(""))  # True
