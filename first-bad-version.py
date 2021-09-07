#!/usr/bin/python3
# https://leetcode.com/problems/first-bad-version/
# 278. First Bad Version


def binary_search(l, r):
    if r >= l:
        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if isBadVersion(mid):
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        # Element is not present in the array
        return -1


def first_bad_version(n: int) -> int:

    return binary_search(0, n - 1)


if __name__ == '__main__':
    print(first_bad_version(5))
    print(first_bad_version(1))
