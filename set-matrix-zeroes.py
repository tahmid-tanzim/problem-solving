#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/set-matrix-zeroes/


def set_zeroes(matrix):
    positions_i, positions_j, m, n = [], [], len(matrix), len(matrix[0])
    i = 0
    while i < m:
        j = 0
        while j < n:
            if matrix[i][j] == 0:
                if i not in positions_i:
                    positions_i.append(i)
                if j not in positions_j:
                    positions_j.append(j)
            j += 1
        i += 1

    for p in positions_i:
        i = 0
        while i < n:
            matrix[p][i] = 0
            i += 1

    for p in positions_j:
        i = 0
        while i < m:
            matrix[i][p] = 0
            i += 1

    print(matrix)


if __name__ == '__main__':
    set_zeroes([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])

    # set_zeroes([
    #     [0, 1, 2, 0],
    #     [3, 4, 5, 2],
    #     [1, 3, 1, 5]
    # ])
    #
    # set_zeroes([
    #     [0, 0, 0, 5],
    #     [4, 3, 1, 4],
    #     [0, 1, 1, 4],
    #     [1, 2, 1, 3],
    #     [0, 0, 1, 1]
    # ])
