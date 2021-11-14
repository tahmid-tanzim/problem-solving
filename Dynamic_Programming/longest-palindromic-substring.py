#!/usr/bin/python3
# https://leetcode.com/problems/longest-palindromic-substring/


# O() time, O() space
class Solution1:
    def __init__(self):
        self._longestSubstring = None

    # def _isPalindrome(self, s: str, leftIdx: int, rightIdx: int):
    #     if leftIdx < 0 or rightIdx >= len(s):
    #         return
    #
    #     if s[leftIdx] == s[rightIdx]:
    #         if rightIdx - leftIdx + 1 > self._longestSubstring["length"]:
    #             self._longestSubstring = dict(length=rightIdx - leftIdx + 1, value=s[leftIdx:rightIdx + 1])
    #         self._isPalindrome(s, leftIdx - 1, rightIdx + 1)

    def _isPalindrome(self, s: str, leftIdx: int, rightIdx: int):
        while leftIdx >= 0 and rightIdx < len(s) and s[leftIdx] == s[rightIdx]:
            if rightIdx - leftIdx + 1 > self._longestSubstring["length"]:
                self._longestSubstring = dict(length=rightIdx - leftIdx + 1, value=s[leftIdx:rightIdx + 1])
            leftIdx -= 1
            rightIdx += 1

    def longestPalindrome(self, string: str) -> str:
        self._longestSubstring = dict(length=0, value="")

        for i in range(len(string)):
            self._isPalindrome(string, i, i)  # ODD Length Palindrome
            self._isPalindrome(string, i, i + 1)  # EVEN Length Palindrome

        return self._longestSubstring["value"]


class Solution2:
    @staticmethod
    def longestPalindrome(string: str) -> str:
        palindromicSubstring = str()
        n = len(string)
        i = 0
        leftPointer = 0
        rightPointer = 0
        while i < n:
            # Check if palindrome string length is ODD
            while (leftPointer >= 0 and rightPointer < n) and string[leftPointer] == string[rightPointer]:
                leftPointer -= 1
                rightPointer += 1
            if len(palindromicSubstring) < (rightPointer - leftPointer - 1):
                palindromicSubstring = string[leftPointer + 1:rightPointer]

            # Check if palindrome string length is EVEN
            leftPointer = i - 1
            rightPointer = i
            while (leftPointer >= 0 and rightPointer < n) and string[leftPointer] == string[rightPointer]:
                leftPointer -= 1
                rightPointer += 1
            if len(palindromicSubstring) < (rightPointer - leftPointer - 1):
                palindromicSubstring = string[leftPointer + 1:rightPointer]

            i += 1
            leftPointer = i
            rightPointer = i

        return palindromicSubstring


if __name__ == '__main__':
    obj = Solution2()
    print(obj.longestPalindrome("babad"))
    print(obj.longestPalindrome("cbbd"))
    print(obj.longestPalindrome("a"))
    print(obj.longestPalindrome("ac"))
