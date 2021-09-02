#!/usr/bin/python3

from itertools import product


def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for x in tuple(product(a, b)):
        print(x, end=' ')


if __name__ == '__main__': main()
