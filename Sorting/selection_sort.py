#!/usr/bin/python3


def selection_sort(A, n, order='ASC'):
    for i in range(n - 1):
        index = i
        for j in range(i + 1, n):
            if A[j] < A[index] and order == 'ASC' or A[j] > A[index] and order == 'DESC':
                index = j

        # Swap with minimum value
        if index != i:
            A[i] = A[i] + A[index]
            A[index] = A[i] - A[index]
            A[i] = A[i] - A[index]
    return A


if __name__ == "__main__":
    output = selection_sort([3, 44, 38, 5, 15, 26, 27, 2, 46, 5, 4], 11, 'DESC')
    print(output)
