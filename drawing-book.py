#!/usr/bin/python3
# https://www.hackerrank.com/challenges/drawing-book/problem


def page_count(n, p):
    return min(p // 2, n // 2 - p // 2)


if __name__ == '__main__':
    for n in range(1, 14):
        print('--------N: {}----------'.format(n))
        for p in range(1, n + 1):
            print('Page ({}): '.format(p), page_count(n, p))


