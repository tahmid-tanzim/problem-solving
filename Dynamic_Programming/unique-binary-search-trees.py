#!/usr/bin/python3
# https://leetcode.com/problems/unique-binary-search-trees/
import time
"""
Formula -
2n C n / n + 1
"""


# O(2^n) time, O(n) space
class Solution1:
    def nCr(self, n: int, r: int, CACHE):
        if r == 0 or n == r:
            return 1

        key = f"{n}:{r}"
        if key in CACHE:
            return CACHE[key]

        CACHE[key] = self.nCr(n - 1, r - 1, CACHE) + self.nCr(n - 1, r, CACHE)
        return CACHE[key]

    def numTrees(self, n: int) -> int:
        return self.nCr(2 * n, n, dict()) // (n + 1)


if __name__ == "__main__":
    obj = Solution1()

    print(obj.numTrees(3))
    # # Output: 5
    #
    print(obj.numTrees(1))
    # # Output: 1
    #
    print(obj.numTrees(4))
    # Output: 14

    start_time = time.time()
    print(obj.numTrees(19))
    # Output: 1767263190
    print("--- %s seconds ---" % (time.time() - start_time))


