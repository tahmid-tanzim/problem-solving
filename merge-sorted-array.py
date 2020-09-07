#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/merge-sorted-array/


def merge_two_array(nums1, m, nums2, n):
    for f, b in zip(nums1, nums2):
        print(f, b)


if __name__ == '__main__':
    merge_two_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
