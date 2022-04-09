#!/usr/bin/python3
# https://leetcode.com/problems/remove-element/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                j = i + 1
                while j < n:
                    temp = nums[j]
                    nums[j] = nums[j - 1]
                    nums[j - 1] = temp
                    j += 1
                n -= 1
            else:
                i += 1
        return n


if __name__ == "__main__":
    s = Solution()
    print(s.removeElement([3, 2, 2, 3], 3))  # 2
    print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))  # 5
