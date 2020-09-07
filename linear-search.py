#!/usr/local/bin/python3.6


def linear_search(A, n, x):
    for i in range(n):
        if A[i] == x:
            return i
    return -1


if __name__ == "__main__":
    output = linear_search([60, 1, 88, 11, 100], 5, 121)
    print(output)