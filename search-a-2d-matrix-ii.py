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
        middle_element = matrix[middle_index // columns][middle_index % columns]
        if middle_element < target:
            left = middle_index + 1
        elif middle_element > target:
            right = middle_index - 1
        else:
            return True
    return False


if __name__ == '__main__':
    print(search_matrix([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 5))
    print(search_matrix([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 20))
