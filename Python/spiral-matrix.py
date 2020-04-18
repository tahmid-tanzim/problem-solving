#!/usr/local/bin/python3.6


def spiral_order(matrix) -> int:
    output = []

    if len(matrix) == 0:
        return output

    row_begin = 0
    row_end = len(matrix) - 1
    col_begin = 0
    col_end = len(matrix[0]) - 1

    while row_begin <= row_end and col_begin <= col_end:
        # Upper Row
        j = col_begin
        while j <= col_end:
            output.append(matrix[row_begin][j])
            j += 1
        row_begin += 1

        # Right Column
        i = row_begin
        while i <= row_end:
            output.append(matrix[i][col_end])
            i += 1
        col_end -= 1

        # Bottom Row
        if row_begin <= row_end:
            j = col_end
            while j >= col_begin:
                output.append(matrix[row_end][j])
                j -= 1
        row_end -= 1

        # Left Column
        if col_begin <= col_end:
            i = row_end
            while i >= row_begin:
                output.append(matrix[i][col_begin])
                i -= 1
        col_begin += 1

    return output


if __name__ == '__main__':
    print(spiral_order([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))

    print(spiral_order([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]))
