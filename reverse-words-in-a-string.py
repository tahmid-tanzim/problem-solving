#!/usr/bin/python3
# https://leetcode.com/problems/reverse-words-in-a-string/


def reverse_words(s: str) -> str:
    startIdx = 0
    endIdx = 0
    reversed_str = ""

    while s[startIdx] == ' ':
        startIdx += 1
        endIdx += 1

    while endIdx < len(s):
        if s[endIdx] == ' ':
            reversed_str = s[startIdx:endIdx] + ' ' + reversed_str
            startIdx = endIdx + 1
            while startIdx < len(s):
                if s[startIdx] != ' ':
                    break
                startIdx += 1
                endIdx += 1
        endIdx += 1

    if s[startIdx:endIdx]:
        reversed_str = s[startIdx:endIdx] + ' ' + reversed_str
    return reversed_str[:-1]


if __name__ == '__main__':
    print(reverse_words("the sky is blue"))
    print(reverse_words("  hello world  "))
    print(reverse_words("a good   example"))
    print(reverse_words("  Bob    Loves  Alice   "))
    print(reverse_words("Alice does not even like bob"))
