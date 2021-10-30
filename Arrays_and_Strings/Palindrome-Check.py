#!/usr/bin/python3
# https://www.algoexpert.io/questions/Palindrome%20Check


def isPalindrome(string):
    mid = len(string) // 2
    i = 0
    while i < mid:
        if string[i] != string[(i + 1) * -1]:
            return False
        i += 1
    return True


if __name__ == '__main__':
    print(isPalindrome("abcdcba"))
