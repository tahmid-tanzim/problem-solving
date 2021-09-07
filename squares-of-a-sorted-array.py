#!/usr/bin/python3
# https://leetcode.com/problems/squares-of-a-sorted-array/


def sorted_squares(A):
    output = []
    for a in A:
        output.append(a * a)
    output.sort()
    return output


if __name__ == '__main__':
    print(sorted_squares([-4, -1, 0, 3, 10])) #[0,1,9,16,100]
    print('********************************')
    print(sorted_squares([-7, -3, 2, 3, 11])) #[4,9,9,49,121]
