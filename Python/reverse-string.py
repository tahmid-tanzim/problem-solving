#!/usr/local/bin/python3


class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        x = len(s)
        i = 0
        while i < x / 2:
            temp = s[i]
            s[i] = s[x - i - 1]
            s[x - i - 1] = temp
            i += 1
        print(s)


if __name__ == "__main__":
    o = Solution()
    o.reverseString(["h", "e", "l", "l", "o"])
    o.reverseString(["H", "a", "n", "n", "a", "h"])
