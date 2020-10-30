#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/merge-sorted-array/
# 88. Merge Sorted Array


def merge_two_array(nums1, m, nums2, n):
    p = 0
    q = 0
    shift_pointer = m
    while q < n:
        while p < m + n:
            if nums1[p] == 0 and p >= shift_pointer:
                nums1[p] = nums2[q]
                p += 1
                shift_pointer += 1
                break
            if nums2[q] < nums1[p]:
                backlog = nums2[q]
                i = p
                while i < m + n:
                    temp = nums1[i]
                    nums1[i] = backlog
                    if temp == 0 and i >= shift_pointer:
                        break
                    backlog = temp
                    i += 1
                shift_pointer += 1
                p += 1
                break
            p += 1
        q += 1
    return nums1


if __name__ == '__main__':
    print(merge_two_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
    print(merge_two_array([0, 0, 0], 0, [2, 5, 6], 3))
    print(merge_two_array([1, 3, 5, 7, 0, 0, 0], 4, [2, 4, 6], 3))
    print(merge_two_array([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3))
    print(merge_two_array([0, 0, 3, 0, 0, 0, 0, 0, 0], 3, [-1, 1, 1, 1, 2, 3], 6))
    print(merge_two_array([-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0], 5, [-1, -1, 0, 0, 1, 2], 6))
