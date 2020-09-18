#!/usr/local/bin/python3
# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1440/


class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        x = len(s)
        i = 0
        while i < x // 2:
            temp = s[i]
            s[i] = s[x - i - 1]
            s[x - i - 1] = temp
            i += 1
        print(s)

    def reverse_str_recursion(self, s, i, n):
        if i >= n:
            return
        else:
            temp = s[i]
            s[i] = s[n]
            s[n] = temp
            self.reverse_str_recursion(s, i + 1, n - 1)
            return s

    def reverse_string(self, s):
        s = self.reverse_str_recursion(s, 0, len(s) - 1)
        print(s)


if __name__ == "__main__":
    o = Solution()
    o.reverseString(["h", "e", "l", "l", "o"])
    o.reverseString(["H", "a", "n", "n", "a", "h"])

    o.reverse_string(["h", "e", "l", "l", "o"])
    o.reverse_string(["H", "a", "n", "n", "a", "h"])
