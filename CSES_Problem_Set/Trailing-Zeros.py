#!/usr/bin/python3
# https://cses.fi/problemset/task/1618

if __name__ == '__main__':
    n = int(input())
    zeros = 0
    i = 5
    while n / i >= 1:
        zeros += int(n / i)
        i *= 5
    print(zeros)
