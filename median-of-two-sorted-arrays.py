#!/usr/bin/python3
# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List


# Brute-Force
# Time Complexity - O(m + n)
# Space Complexity - O(m + n)
# m is the length of num1, n is the length of num2
class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0
        mergedArray = list()
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                mergedArray.append(nums1[p1])
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                mergedArray.append(nums2[p2])
                p2 += 1
            else:
                mergedArray.append(nums1[p1])
                p1 += 1
                mergedArray.append(nums2[p2])
                p2 += 1
        mergedArray += nums1[p1:]
        mergedArray += nums2[p2:]
        # print(mergedArray)
        mergedArrayLength = len(mergedArray)
        midIdx = mergedArrayLength // 2
        if mergedArrayLength % 2 == 0:
            return (mergedArray[midIdx] + mergedArray[midIdx - 1]) / 2
        else:
            return float(mergedArray[midIdx])


# Optimal Solution
# Time Complexity - O(log(m + n))
# Space Complexity - O(1)
# m is the length of num1, n is the length of num2
class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalArrayLength = len(nums1) + len(nums2)
        midIdx = totalArrayLength // 2
        i = 0
        j = 0
        secondMiddleValue, firstMiddleValue = 0, 0
        while i < len(nums1) and j < len(nums2) and midIdx >= 0:
            if nums1[i] < nums2[j]:
                firstMiddleValue = secondMiddleValue
                secondMiddleValue = nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                firstMiddleValue = secondMiddleValue
                secondMiddleValue = nums2[j]
                j += 1
            else:
                secondMiddleValue = nums1[i]
                i += 1
                midIdx -= 1
                if midIdx < 0:
                    break
                firstMiddleValue = nums2[j]
                j += 1
            midIdx -= 1

        while i < len(nums1) and midIdx >= 0:
            firstMiddleValue = secondMiddleValue
            secondMiddleValue = nums1[i]
            i += 1
            midIdx -= 1

        while j < len(nums2) and midIdx >= 0:
            firstMiddleValue = secondMiddleValue
            secondMiddleValue = nums2[j]
            j += 1
            midIdx -= 1

        if totalArrayLength % 2 == 0:
            return (firstMiddleValue + secondMiddleValue) / 2
        else:
            return float(secondMiddleValue)


if __name__ == '__main__':
    obj = Solution2()
    print(obj.findMedianSortedArrays([1, 3], [2]))  # 2.0
    print(obj.findMedianSortedArrays([1, 2], [3, 4]))  # 2.50
    print(obj.findMedianSortedArrays([0, 0], [0, 0]))  # 0.00
    print(obj.findMedianSortedArrays([], [1]))  # 1.00
    print(obj.findMedianSortedArrays([2], []))  # 2.00
    print(obj.findMedianSortedArrays([1, 3, 4, 7, 10, 12], [2, 3, 6, 15]))  # 5.00
    print(obj.findMedianSortedArrays([2, 2, 4, 4], [2, 2, 4, 4]))  # 3.00

