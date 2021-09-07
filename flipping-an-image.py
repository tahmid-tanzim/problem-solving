#!/usr/bin/python3
# https://leetcode.com/problems/flipping-an-image/


def flip_and_invert_image(A):
    output = []
    for a in A:
        i, x = len(a) - 1, []
        while i >= 0:
            x.append(1 - a[i])
            i -= 1
        output.append(x)
    return output


if __name__ == '__main__':
    print(flip_and_invert_image([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
    print(flip_and_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
