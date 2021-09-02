#!/usr/bin/python3
# https://leetcode.com/problems/climbing-stairs/


class Solution:
    def __init__(self) -> None:
        self.lookup = [-1] * 46

    def climb_stairs(self, n: int) -> int:
        if n == 1 or n == 2:
            self.lookup[n] = n

        if self.lookup[n] == -1:
            self.lookup[n] = self.climb_stairs(n - 1) + self.climb_stairs(n - 2)

        return self.lookup[n]


if __name__ == "__main__":
    s = Solution()
    print(s.climb_stairs(5))
