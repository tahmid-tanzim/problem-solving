#!/usr/bin/python3
# https://leetcode.com/problems/n-th-tribonacci-number/


# Top Down, Memoization
# O(n) time, O(n) space
class Solution1:
    def tribonacci(self, n: int, cache: dict = {}) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        if n in cache:
            return cache[n]
        cache[n] = self.tribonacci(n - 1, cache) + self.tribonacci(n - 2, cache) + self.tribonacci(n - 3, cache)
        return cache[n]


# Bottom UP, Tabulation
# O(n) time, O(1) space
class Solution2:
    def tribonacci(self, n: int) -> int:
        T = [0, 1, 1]
        if n <= 2:
            return T[n]

        for i in range(3, n):
            temp = sum(T)
            T[0] = T[1]
            T[1] = T[2]
            T[2] = temp

        return sum(T)


if __name__ == "__main__":
    obj = Solution1()
    print(obj.tribonacci(4))  # 4
    print(obj.tribonacci(25))  # 1389537
