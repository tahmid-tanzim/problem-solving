#!/usr/local/bin/python3.6


if __name__ == '__main__':
    n = input()
    x = input().split()
    print(all(list(map(lambda s: int(s) > 0, x))) and any(list(map(lambda s: s == s[::-1], x))))
