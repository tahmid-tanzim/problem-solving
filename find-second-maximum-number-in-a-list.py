#!/usr/local/bin/python3.6


def main():
    n = 5  # int(input())
    arr = [2, 3, 6, 6, 5]  # map(int, input().split())
    first = second = -101

    for i in arr:
        if i > first:
            second, first = first, i
        elif i > second and i != first:
            second = i

    print(first, second)


if __name__ == '__main__': main()
