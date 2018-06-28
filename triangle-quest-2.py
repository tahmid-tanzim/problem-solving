#!/usr/local/bin/python3.6


if __name__ == '__main__':
    for i in range(1, int(input()) + 1):
        # print(i, list(map(lambda x: 10 ** x, range(2 * i - 1))))
        print(((10 ** i - 1) // 9) ** 2)

