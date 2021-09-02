#!/usr/bin/python3


def generate_matrix(n) -> int:
    # Initialize 2D Array
    matrix = [[None] * n for _ in range(n)]
    counter = 1
    row_begin = 0
    row_end = n - 1
    col_begin = 0
    col_end = n - 1

    while row_begin <= row_end and col_begin <= col_end:
        # Top Row
        j = col_begin
        while j <= col_end:
            matrix[row_begin][j] = counter
            counter += 1
            j += 1
        row_begin += 1

        # Right Column
        i = row_begin
        while i <= row_end:
            matrix[i][col_end] = counter
            counter += 1
            i += 1
        col_end -= 1

        # Bottom Row
        j = col_end
        while j >= col_begin:
            matrix[row_end][j] = counter
            counter += 1
            j -= 1
        row_end -= 1

        # Left Column
        i = row_end
        while i >= row_begin:
            matrix[i][col_begin] = counter
            counter += 1
            i -= 1
        col_begin += 1
    return matrix


if __name__ == '__main__':
    # print(generate_matrix(3))
    # print(generate_matrix(5))
    print(generate_matrix(1))
