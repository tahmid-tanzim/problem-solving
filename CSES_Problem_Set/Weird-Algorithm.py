#!/usr/bin/python3
# https://cses.fi/problemset/task/1068/


def function(n):
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(1)


if __name__ == '__main__':
    num = int(input())
    function(num)
