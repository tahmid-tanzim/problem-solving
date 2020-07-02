#!/usr/local/bin/python3
# https://leetcode.com/problems/valid-anagram/


def is_anagram(s, t):
    if len(s) != len(t):
        return False

    hash_table = {}
    for char in s:
        if char not in hash_table:
            hash_table[char] = 1
        else:
            hash_table[char] += 1

    for char in t:
        if char not in hash_table:
            return False
        else:
            hash_table[char] -= 1
            if hash_table[char] < 0:
                return False

    return True
    # return True if sum(hash_table.values()) == 0 else False


if __name__ == '__main__':
    # print(is_anagram(s="anagram", t="nagaram"))  # True
    # print(is_anagram(s="rat", t="car"))  # False
    print(is_anagram(s="aacc", t="ccac"))  # False
