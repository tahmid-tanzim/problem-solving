#!/usr/local/bin/python3.6


def binary_search(A, n, x):
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) / 2

        if A[mid] == x:
            return mid

        if A[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    output = binary_search([1, 4, 6, 7, 10, 19, 22, 23, 30, 35, 39, 46, 49, 50, 52, 55, 61, 67, 70, 71], 20, 7)
    print(output)