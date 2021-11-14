#!/usr/bin/python3
# https://leetcode.com/problems/palindromic-substrings/


# Top Down, Memoization
# O() time, O() space
class Solution1:
    def __init__(self):
        self.counter = -1

    def isPalindrome(self, s: str, leftIdx: int, rightIdx: int):
        if leftIdx < 0 or rightIdx >= len(s):
            return

        if s[leftIdx] == s[rightIdx]:
            self.counter += 1
            self.isPalindrome(s, leftIdx - 1, rightIdx + 1)

    # def isPalindrome(self, s: str, leftIdx: int, rightIdx: int):
    #     while leftIdx >= 0 and rightIdx < len(s) and s[leftIdx] == s[rightIdx]:
    #         self.counter += 1
    #         leftIdx -= 1
    #         rightIdx += 1

    def countSubstrings(self, s: str) -> int:
        self.counter = 0

        for i in range(len(s)):
            self.isPalindrome(s, i, i)  # ODD Length Palindrome
            self.isPalindrome(s, i, i + 1)  # EVEN Length Palindrome

        return self.counter


if __name__ == '__main__':
    obj = Solution1()
    print(obj.countSubstrings("abc"))
    print(obj.countSubstrings("aaa"))
    print(obj.countSubstrings("abaab"))
