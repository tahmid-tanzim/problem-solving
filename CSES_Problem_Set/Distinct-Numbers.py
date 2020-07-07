#!/usr/local/bin/python3
# https://cses.fi/problemset/task/1621

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))

    x.sort()
    xi = distinct_count = 0
    for i in x:
        if xi != i:
            xi = i
            distinct_count += 1
    print(distinct_count)

