#!/usr/bin/python3
# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List


# O(nlog(n)) time, O(1) space
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]


if __name__ == "__main__":
    obj = Solution1()

    print(obj.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(obj.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
