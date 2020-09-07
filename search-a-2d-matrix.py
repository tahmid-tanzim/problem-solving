#!/usr/local/bin/python3.6


def search_matrix(matrix, target):
    if len(matrix) == 0:
        return False

    rows = len(matrix)
    columns = len(matrix[0])

    left = 0
    right = rows * columns - 1

    while left <= right:
        middle_index = left + (right - left) // 2
        middle_element = matrix[middle_index//columns][middle_index%columns]
        if middle_element < target:
            left = middle_index + 1
        elif middle_element > target:
            right = middle_index - 1
        else:
            return True
    return False


if __name__ == '__main__':
    print(search_matrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 3))
    print(search_matrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 13))
