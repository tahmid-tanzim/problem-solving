#!/usr/bin/python3
# https://leetcode.com/problems/remove-vowels-from-a-string/


def remove_vowels(S):
    output, vowels = "", ('a', 'e', 'i', 'o', 'u')
    for s in S:
        if s not in vowels:
            output += s
    return output


if __name__ == '__main__':
    print(remove_vowels("leetcodeisacommunityforcoders"))
    print(remove_vowels("aeiou"))
