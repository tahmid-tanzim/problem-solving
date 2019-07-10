#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/transpose-matrix/


def transpose(A):
    r, output = 0, []
    while r < len(A):
        c = 0
        while c < len(A[r]):
            if r > 0:
                output[c].append(A[r][c])
            else:
                output.append([A[r][c]])
            c += 1
        r += 1
    return output


if __name__ == '__main__':
    print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(transpose([[1, 2, 3], [4, 5, 6]]))
