#!/usr/bin/python3
# https://cses.fi/problemset/task/1094

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    diff, i = 0, 1
    while i < n:
        d = array[i - 1] - array[i]
        if d > 0:
            array[i] += d
            diff += d
        i += 1
    print(diff)

