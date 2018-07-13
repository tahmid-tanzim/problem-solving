#!/usr/local/bin/python3.6


def selection_sort(A, n):
    for i in range(n - 1):
        index_min = i
        for j in range(i + 1, n):
            if A[j] < A[index_min]:
                index_min = j

        # Swap with minimum value
        if index_min != i:
            A[i] = A[i] + A[index_min]
            A[index_min] = A[i] - A[index_min]
            A[i] = A[i] - A[index_min]
    return A


if __name__ == "__main__":
    output = selection_sort([3, 44, 38, 5, 15, 26, 27, 2, 46, 5, 4], 11)
    print(output)