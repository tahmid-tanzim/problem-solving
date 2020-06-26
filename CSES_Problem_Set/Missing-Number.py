#!/usr/local/bin/python3
# https://cses.fi/problemset/task/1083

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    print(sum(range(n + 1)) - sum(array))
