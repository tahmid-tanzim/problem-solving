#!/usr/bin/python3
# https://leetcode.com/problems/longest-palindrome/

def longestPalindrome(s: str) -> int:
    hashtable = {}
    for char in s:
        if char not in hashtable:
            hashtable[char] = 0
        hashtable[char] += 1
    total_char = 0
    odd_counter = 0

    for char in hashtable:
        total_char += hashtable[char]
        if hashtable[char] % 2 == 1:
            odd_counter += 1
    if odd_counter > 0:
        total_char -= odd_counter - 1
    return total_char
